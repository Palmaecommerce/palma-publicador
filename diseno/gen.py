import asyncio, os, json
from playwright.async_api import async_playwright
from PIL import Image
import sys
mod=__import__(sys.argv[1] if len(sys.argv)>1 else 'contenido')
C,WA=mod.C,mod.WA
FONT="/home/claude/planes-img/node_modules/@fontsource/poppins/files/poppins-latin-%s-normal.woff2"
ICON="/home/claude/logo/final/palma-icono-1024.png"
CSS="""@font-face{font-family:P;src:url(F4);font-weight:400}@font-face{font-family:P;src:url(F6);font-weight:600}@font-face{font-family:P;src:url(F8);font-weight:800}
*{margin:0;box-sizing:border-box}body{width:Wpx;height:Hpx;font-family:P;overflow:hidden;position:relative;padding:90px 84px}
.dark{color:#fff;background:radial-gradient(circle at 92% 6%,#D61F72 0,rgba(214,31,114,.45) 24%,rgba(43,20,82,0) 58%),radial-gradient(circle at 0 100%,rgba(233,71,42,.5) 0,rgba(43,20,82,0) 46%),#2B1452}
.light{color:#2B1452;background:#F7F4F1}
.top{display:flex;align-items:center;gap:16px;font-weight:800;font-size:30px}.top img{width:58px;height:58px;border-radius:14px}
.num{position:absolute;top:100px;right:84px;font-weight:600;font-size:26px;opacity:.6}
.kick{display:inline-block;margin-top:110px;background:#E9472A;color:#fff;border-radius:999px;padding:12px 28px;font-weight:800;font-size:26px;letter-spacing:2px}
.big{font-size:108px;line-height:1.02;font-weight:800;margin-top:34px;letter-spacing:-2px}.big span{color:#FFB3C7}
.swipe{position:absolute;bottom:90px;left:84px;font-weight:600;font-size:30px;opacity:.85}
h2{font-size:84px;line-height:1.06;font-weight:800;margin-top:150px;letter-spacing:-1px}
.light h2{color:#2B1452}.light h2:before{content:"";display:block;width:90px;height:10px;border-radius:9px;background:linear-gradient(90deg,#E9472A,#D61F72);margin-bottom:34px}
ul{list-style:none;padding:0;margin-top:64px;display:flex;flex-direction:column;gap:26px}
li{font-size:46px;line-height:1.3;font-weight:600;padding:34px 38px;background:#fff;border-radius:24px;box-shadow:0 8px 24px rgba(43,20,82,.08)}
.cta h2{margin-top:200px;font-size:86px}.cta p{font-size:42px;line-height:1.35;margin-top:36px;color:#F1ECF4}
.btn{position:absolute;left:84px;right:84px;bottom:190px;background:#fff;color:#2B1452;border-radius:999px;text-align:center;font-weight:800;font-size:42px;padding:34px}
.foot{position:absolute;left:84px;right:84px;bottom:110px;text-align:center;font-size:26px;font-weight:600;letter-spacing:1px;color:#F1ECF4}
.story .kick{margin-top:260px}.story .big{font-size:110px}.story p{font-size:46px;line-height:1.35;margin-top:44px;color:#F1ECF4}
.pie{position:absolute;left:84px;right:84px;bottom:80px;display:flex;justify-content:space-between;font-size:26px;font-weight:600;color:#8a7aa3}
.compact ul{gap:18px;margin-top:48px}.compact li{font-size:38px;padding:24px 30px}
.badge{position:absolute;top:190px;left:84px;background:#D61F72;color:#fff;border-radius:999px;padding:10px 26px;font-weight:800;font-size:26px;letter-spacing:2px}
.badge+h2:before{display:none}.badge+h2{margin-top:200px}
.story .btn{bottom:330px}.story .foot{bottom:250px}
"""
for k,v in (("F4",400),("F6",600),("F8",800)): CSS=CSS.replace(k,FONT%v)
TOP=f'<div class=top><img src="{ICON}">Palma Ecommerce</div>'
def cover(c,n): a,b,d=c["cover"]; return f'<body class=dark>{TOP}<div class=num>1/{n}</div><div class=kick>{c["kicker"]}</div><div class=big>{a} {b} <span>{d}</span></div><div class=swipe>Deslizá →</div></body>'
def slide(t,items,i,n,badge=''):
    cls='light compact' if len(items)>=4 or sum(len(x) for x in items)>150 else 'light'
    bd=f'<div class=badge>{badge}</div>' if badge else ''
    return f'<body class="{cls}">{TOP}<div class=num>{i}/{n}</div>{bd}<h2>{t}</h2><ul>'+''.join(f'<li>{x}</li>' for x in items)+'</ul><div class=pie><span>Partner certificado de Tiendanube</span><span>Deslizá →</span></div></body>'
def cta(c,i,n): t,p=c["cta"]; return f'<body class="dark cta">{TOP}<div class=num>{i}/{n}</div><h2>{t}</h2><p>{p}</p><div class=btn>WhatsApp {WA}</div><div class=foot>PARTNER CERTIFICADO DE TIENDANUBE</div></body>'
def story(c): t,p=c["historia"]; return f'<body class="dark story">{TOP}<div class=kick>NUEVO POST</div><div class=big>{t}</div><p>{p}</p><div class=btn>WhatsApp {WA}</div><div class=foot>@palma.ecommerce</div></body>'
async def shot(b,html,w,h,out):
    pg=await b.new_page(viewport={'width':w,'height':h})
    open(out+'.html','w').write(f'<html><head><meta charset=utf-8><style>{CSS.replace("Wpx",f"{w}px").replace("Hpx",f"{h}px")}</style></head>{html}</html>')
    await pg.goto('file://'+os.path.abspath(out+'.html'))
    await pg.wait_for_timeout(300); await pg.screenshot(path=out+'.png'); await pg.close()
    Image.open(out+'.png').convert('RGB').save(out+'.jpg',quality=92); os.remove(out+'.png'); os.remove(out+'.html')
async def main():
    os.makedirs('out',exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for c in C:
            n=len(c["slides"])+2; files=[]
            await shot(b,cover(c,n),1080,1350,f'out/{c["id"]}-01'); files.append(f'{c["id"]}-01.jpg')
            for i,sl in enumerate(c["slides"],2):
                await shot(b,slide(sl[0],sl[1],i,n,*(sl[2:] or [''])),1080,1350,f'out/{c["id"]}-{i:02d}'); files.append(f'{c["id"]}-{i:02d}.jpg')
            await shot(b,cta(c,n,n),1080,1350,f'out/{c["id"]}-{n:02d}'); files.append(f'{c["id"]}-{n:02d}.jpg')
            await shot(b,story(c),1080,1920,f'out/{c["id"]}-historia'); c["files"]=files
        await b.close()
    # hojas de vista previa (todas las placas de un carrusel + historia)
    for c in C:
        ims=[Image.open('out/'+f) for f in c["files"]]; st=Image.open(f'out/{c["id"]}-historia.jpg')
        w=360; h=450; cols=4; rows=(len(ims)+cols-1)//cols
        sheet=Image.new('RGB',(cols*w+ (w*1080//1920*0+260) ,max(rows*h,640)),'#e9e4ee')
        for k,im in enumerate(ims): sheet.paste(im.resize((w,h)),((k%cols)*w,(k//cols)*h))
        sheet.paste(st.resize((240,427)),(cols*w+10,10)); sheet.save(f'out/vista-{c["id"]}.png')
    prev=json.load(open('out/archivos.json')) if os.path.exists('out/archivos.json') else {}
    prev.update({c["id"]:c["files"] for c in C}); json.dump(prev,open('out/archivos.json','w'),indent=1)
asyncio.run(main())
