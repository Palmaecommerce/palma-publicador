import asyncio, os, sys, json
from playwright.async_api import async_playwright
from PIL import Image
FONT="/home/claude/planes-img/node_modules/@fontsource/poppins/files/poppins-latin-%s-normal.woff2"
ICON="/home/claude/logo/final/palma-icono-1024.png"
CSS="""@font-face{font-family:P;src:url(F4);font-weight:400}@font-face{font-family:P;src:url(F6);font-weight:600}@font-face{font-family:P;src:url(F8);font-weight:800}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:P;overflow:hidden;position:relative;padding:80px 80px}
.dark{color:#fff;background:radial-gradient(circle at 95% 4%,#D61F72 0,rgba(214,31,114,.5) 26%,rgba(43,20,82,0) 60%),radial-gradient(circle at 0 100%,rgba(233,71,42,.55) 0,rgba(43,20,82,0) 48%),#2B1452}
.light{color:#2B1452;background:#F7F4F1}
.top{display:flex;align-items:center;gap:14px;font-weight:800;font-size:28px}.top img{width:54px;height:54px;border-radius:13px}
.bar{position:absolute;top:0;left:0;height:12px;background:linear-gradient(90deg,#E9472A,#D61F72)}
.pg{position:absolute;top:92px;right:80px;font-weight:800;font-size:26px;opacity:.55}
.k{display:inline-block;background:#E9472A;color:#fff;border-radius:999px;padding:12px 28px;font-weight:800;font-size:26px;letter-spacing:2px}
.h{font-weight:800;letter-spacing:-2px;line-height:1.02}.h span{color:#FF8FB1}.light .h span{color:#D61F72}
.sub{font-size:42px;line-height:1.3;font-weight:600}
.next{position:absolute;left:80px;right:80px;bottom:70px;display:flex;align-items:center;justify-content:space-between;gap:20px;border-radius:28px;padding:30px 36px;font-weight:800;font-size:36px}
.dark .next{background:#fff;color:#2B1452}.light .next{background:#2B1452;color:#fff}
.next b{font-size:54px;line-height:1}
.n{font-size:230px;font-weight:800;line-height:.9;color:#E9472A;letter-spacing:-8px}
.chat{background:#E7DED6;border-radius:36px;padding:34px;display:flex;flex-direction:column;gap:18px}
.b{max-width:78%;border-radius:22px;padding:18px 24px;font-size:34px;font-weight:600;color:#1f1f1f;background:#fff;box-shadow:0 2px 0 rgba(0,0,0,.08)}
.b.me{align-self:flex-end;background:#D9FDD3}
.audio{display:flex;align-items:center;gap:16px}.audio i{display:inline-block;width:46px;height:46px;border-radius:50%;background:#2B1452}
.wave{flex:1;height:10px;border-radius:9px;background:repeating-linear-gradient(90deg,#8a8a8a 0 6px,transparent 6px 12px)}
.t{font-size:26px;color:#666}
.card{background:#fff;border-radius:30px;padding:36px 40px;box-shadow:0 14px 40px rgba(43,20,82,.12)}
"""
for k,v in (("F4",400),("F6",600),("F8",800)): CSS=CSS.replace(k,FONT%v)
def page(cls,i,n,body,nxt):
    nx=f'<div class=next><span>{nxt}</span><b>→</b></div>' if nxt else ''
    return f'<body class={cls}><div class=bar style="width:{100*i/n:.0f}%"></div><div class=top><img src="{ICON}">Palma Ecommerce</div><div class=pg>{i}/{n}</div>{body}{nx}</body>'
async def render(slides,prefix):
    os.makedirs('out',exist_ok=True); outs=[]
    async with async_playwright() as p:
        b=await p.chromium.launch(); n=len(slides)
        for i,(cls,body,nxt) in enumerate(slides,1):
            f=f'out/{prefix}-{i:02d}'
            open(f+'.html','w').write(f'<html><head><meta charset=utf-8><style>{CSS}</style></head>{page(cls,i,n,body,nxt)}</html>')
            pg=await b.new_page(viewport={'width':1080,'height':1350}); await pg.goto('file://'+os.path.abspath(f+'.html')); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f+'.png'); await pg.close(); os.remove(f+'.html')
            Image.open(f+'.png').convert('RGB').save(f+'.jpg',quality=92); outs.append(f+'.png')
        await b.close()
    return outs
CSS+=""".chk[style] div{padding:18px 28px;font-size:36px}
.steps{display:flex;gap:22px;margin-top:60px}.st{flex:1;border-radius:26px;padding:26px 20px;background:rgba(255,255,255,.12);border:2px solid rgba(255,255,255,.2);text-align:center;font-weight:800;font-size:30px}
.st b{display:block;font-size:64px;color:#FF8FB1;line-height:1.1}
.chk{display:flex;flex-direction:column;gap:20px;margin-top:46px}.chk div{display:flex;align-items:center;gap:22px;background:#fff;border-radius:24px;padding:26px 30px;font-size:40px;font-weight:600;box-shadow:0 10px 30px rgba(43,20,82,.1)}
.chk i{flex:none;width:52px;height:52px;border-radius:50%;background:#D61F72;position:relative}.chk i:after{content:"";position:absolute;left:18px;top:10px;width:12px;height:24px;border:solid #fff;border-width:0 6px 6px 0;transform:rotate(45deg)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:36px;width:700px}.tile{background:#fff;border-radius:24px;padding:16px;color:#2B1452}.tile .im{height:95px;border-radius:16px;background:linear-gradient(135deg,#F1ECF4,#e3d6ea)}.tile .l1{height:16px;width:80%;background:#e6e0ea;border-radius:8px;margin-top:14px}.tile .pr{font-weight:800;font-size:26px;margin-top:10px;color:#D61F72}
"""
CSS+=""".cli{display:flex;flex-direction:column;gap:16px;margin-top:40px}.cli div{display:flex;align-items:center;gap:20px;background:#fff;border-radius:22px;padding:20px 26px;box-shadow:0 10px 30px rgba(43,20,82,.1)}
.av{flex:none;width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#E9472A,#D61F72);color:#fff;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center}
.cli b{font-size:34px;display:block}.cli span{font-size:26px;color:#7a6b8f;font-weight:600}
.cup{margin-top:50px;border:5px dashed #FF8FB1;border-radius:34px;padding:44px;text-align:center}.cup b{display:block;font-size:110px;letter-spacing:4px;color:#fff}.cup span{font-size:38px;font-weight:600;color:#F1ECF4}
"""
