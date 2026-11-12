"""Robot de publicación de Palma Ecommerce (token de usuario del sistema de Meta, no vence).

Publica en Instagram (API oficial con login de Instagram) y, si hay token de página,
en Facebook. Lee calendario.json, publica lo que ya tiene la hora cumplida y
guarda lo publicado en data/estado.json. Con el argumento "estadisticas" baja las
métricas de cada publicación a data/estadisticas.json.

Secretos (GitHub > Settings > Secrets and variables > Actions):
  IG_TOKEN       token de Instagram (obligatorio)
  FB_PAGE_TOKEN  token de la página de Facebook (opcional)
  FB_PAGE_ID     id de la página de Facebook (opcional)
"""
import json, os, sys, time, datetime as dt, urllib.request, urllib.parse

IG = "https://graph.facebook.com/v23.0"
IG_USER = os.environ.get("IG_USER_ID", "17841414669238656")
FB = "https://graph.facebook.com/v23.0"
REPO = os.environ.get("GITHUB_REPOSITORY", "Palmaecommerce/palma-publicador")
RAW = f"https://raw.githubusercontent.com/{REPO}/main/media/"
TOKEN = os.environ.get("IG_TOKEN", "")
FB_TOKEN = os.environ.get("FB_PAGE_TOKEN", "")
FB_PAGE = os.environ.get("FB_PAGE_ID", "1389049390961304")
ESTADO = "data/estado.json"
STATS = "data/estadisticas.json"


def api(method, url, **params):
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{e.code} {url}: {e.read().decode()[:500]}")


def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def save(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def url(nombre):
    return nombre if nombre.startswith("http") else RAW + urllib.parse.quote(nombre)


def esperar(cid):
    for _ in range(60):
        s = api("GET", f"{IG}/{cid}", fields="status_code", access_token=TOKEN)
        if s.get("status_code") == "FINISHED":
            return
        if s.get("status_code") == "ERROR":
            raise RuntimeError(f"El contenedor {cid} dio error: {s}")
        time.sleep(10)
    raise RuntimeError(f"El contenedor {cid} no terminó de procesar")


def publicar_ig(p):
    tipo, texto = p["tipo"], p.get("texto", "")
    if tipo == "carrusel":
        hijos = []
        for img in p["imagenes"]:
            c = api("POST", f"{IG}/{IG_USER}/media", image_url=url(img), is_carousel_item="true", access_token=TOKEN)
            hijos.append(c["id"])
        for h in hijos:
            esperar(h)
        c = api("POST", f"{IG}/{IG_USER}/media", media_type="CAROUSEL", children=",".join(hijos), caption=texto, access_token=TOKEN)
    elif tipo == "imagen":
        c = api("POST", f"{IG}/{IG_USER}/media", image_url=url(p["imagenes"][0]), caption=texto, access_token=TOKEN)
    elif tipo == "historia":
        if p.get("video"):
            c = api("POST", f"{IG}/{IG_USER}/media", media_type="STORIES", video_url=url(p["video"]), access_token=TOKEN)
        else:
            c = api("POST", f"{IG}/{IG_USER}/media", media_type="STORIES", image_url=url(p["imagenes"][0]), access_token=TOKEN)
    elif tipo == "reel":
        extra = {"cover_url": url(p["portada"])} if p.get("portada") else {}
        c = api("POST", f"{IG}/{IG_USER}/media", media_type="REELS", video_url=url(p["video"]), caption=texto, share_to_feed="true", access_token=TOKEN, **extra)
    else:
        raise RuntimeError(f"Tipo desconocido: {tipo}")
    esperar(c["id"])
    r = api("POST", f"{IG}/{IG_USER}/media_publish", creation_id=c["id"], access_token=TOKEN)
    return r["id"]


def page_token():
    global FB_TOKEN
    if not FB_TOKEN and TOKEN:
        try:
            FB_TOKEN = api("GET", f"{FB}/{FB_PAGE}", fields="access_token", access_token=TOKEN).get("access_token", "")
        except Exception as e:
            print("Sin token de página:", e)
    return FB_TOKEN


def publicar_fb(p):
    page_token()
    if not (FB_TOKEN and FB_PAGE) or not p.get("facebook", True) or p["tipo"] == "historia":
        return None
    texto = p.get("texto", "")
    if p["tipo"] == "reel":
        r = api("POST", f"{FB}/{FB_PAGE}/videos", file_url=url(p["video"]), description=texto, access_token=FB_TOKEN)
        return r.get("id")
    fotos = []
    for img in p["imagenes"]:
        r = api("POST", f"{FB}/{FB_PAGE}/photos", url=url(img), published="false", access_token=FB_TOKEN)
        fotos.append(r["id"])
    params = {"message": texto, "access_token": FB_TOKEN}
    for i, f in enumerate(fotos):
        params[f"attached_media[{i}]"] = json.dumps({"media_fbid": f})
    r = api("POST", f"{FB}/{FB_PAGE}/feed", **params)
    return r.get("id")


def publicar():
    if not TOKEN:
        sys.exit("Falta el secreto IG_TOKEN")
    cal = load("calendario.json", [])
    estado = load(ESTADO, {})
    ahora = dt.datetime.now(dt.timezone.utc)
    errores = []
    for p in sorted(cal, key=lambda x: x["fecha"]):
        if p["id"] in estado or not p.get("aprobado", True):
            continue
        if dt.datetime.fromisoformat(p["fecha"]) > ahora:
            continue
        print("Publicando", p["id"], p["tipo"])
        try:
            ig = publicar_ig(p)
            fb = None
            try:
                fb = publicar_fb(p)
            except Exception as e:
                errores.append(f"Facebook {p['id']}: {e}")
            estado[p["id"]] = {"ig_id": ig, "fb_id": fb, "tipo": p["tipo"], "tema": p.get("tema", ""),
                              "fecha_programada": p["fecha"], "publicado": ahora.isoformat()}
            save(ESTADO, estado)
        except Exception as e:
            errores.append(f"Instagram {p['id']}: {e}")
    if errores:
        sys.exit("\n".join(errores))


METRICAS = {
    "carrusel": "reach,views,likes,comments,saved,shares,total_interactions,follows,profile_visits",
    "imagen": "reach,views,likes,comments,saved,shares,total_interactions,follows,profile_visits",
    "reel": "reach,views,likes,comments,saved,shares,total_interactions,ig_reels_avg_watch_time,ig_reels_video_view_total_time",
    "historia": "reach,views,replies,shares,total_interactions,navigation",
}


def estadisticas():
    estado = load(ESTADO, {})
    stats = load(STATS, {})
    for pid, e in estado.items():
        metricas = METRICAS.get(e["tipo"], METRICAS["imagen"])
        datos = {}
        for m in metricas.split(","):
            try:
                r = api("GET", f"{IG}/{e['ig_id']}/insights", metric=m, access_token=TOKEN)
                for d in r.get("data", []):
                    v = d.get("values", [{}])[0].get("value", d.get("total_value", {}).get("value"))
                    datos[d["name"]] = v
            except Exception as ex:
                datos.setdefault("_sin_dato", []).append(m)
        stats[pid] = {**e, "metricas": datos, "actualizado": dt.datetime.now(dt.timezone.utc).isoformat()}
    try:
        cuenta = api("GET", f"{IG}/{IG_USER}", fields="username,followers_count,media_count", access_token=TOKEN)
        stats["_cuenta"] = cuenta
    except Exception:
        pass
    save(STATS, stats)


def renovar():
    r = api("GET", f"{IG}/refresh_access_token", grant_type="ig_refresh_token", access_token=TOKEN)
    print("::add-mask::" + r["access_token"])
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"token={r['access_token']}\n")


if __name__ == "__main__":
    accion = sys.argv[1] if len(sys.argv) > 1 else "publicar"
    {"publicar": publicar, "estadisticas": estadisticas, "renovar": renovar}[accion]()
