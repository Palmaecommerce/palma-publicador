"""Borra publicaciones duplicadas de Instagram, de a una y despacio.
Antes de borrar cada una verifica que el texto empiece igual que el original
y que no sea una de las que se conservan. Corta ante el primer error."""
import json, os, sys, time, urllib.request, urllib.parse
IG = "https://graph.facebook.com/v23.0"
TOKEN = os.environ["IG_TOKEN"]
MAX = int(os.environ.get("MAX", "5"))
PAUSA = int(os.environ.get("PAUSA", "90"))
d = json.load(open("data/borrar.json"))
hechos = set(json.load(open("data/borrados.json"))) if os.path.exists("data/borrados.json") else set()
conservar = set(d["conservar"].values())
def call(method, path, **q):
    q["access_token"] = TOKEN
    url = f"{IG}/{path}?" + urllib.parse.urlencode(q)
    req = urllib.request.Request(url, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode()[:400]}
n = 0
for inicio, ids in d["borrar"].items():
    for mid in ids:
        if mid in hechos or mid in conservar: continue
        if n >= MAX: break
        info = call("GET", mid, fields="caption")
        if "error" in info:
            if "does not exist" in info["error"] or '"code":100' in info["error"]:
                print("Ya no existe", mid); hechos.add(mid); continue
            print("Error leyendo", mid, info["error"]); n = MAX; break
        if not (info.get("caption") or "").startswith(inicio):
            print("No coincide el texto, no lo borro:", mid); continue
        r = call("DELETE", mid)
        print("Borrar", mid, inicio, "->", r)
        if r.get("success"): hechos.add(mid); n += 1; time.sleep(PAUSA)
        else: n = MAX; break
json.dump(sorted(hechos), open("data/borrados.json", "w"))
total = sum(len(v) for v in d["borrar"].values())
print(f"Borrados en total: {len(hechos)} de {total}")
