import asyncio, os, sys, subprocess, shutil
from playwright.async_api import async_playwright
FONT="/home/claude/planes-img/node_modules/@fontsource/poppins/files/poppins-latin-%s-normal.woff2"
ICON="/home/claude/logo/final/palma-icono-1024.png"
W,H=540,960  # se graba a la mitad y se escala a 1080x1920
CSS=f"""@font-face{{font-family:P;src:url({FONT%600});font-weight:600}}@font-face{{font-family:P;src:url({FONT%800});font-weight:800}}
*{{margin:0;box-sizing:border-box}}body{{width:{W}px;height:{H}px;overflow:hidden;font-family:P;color:#fff;
background:radial-gradient(circle at 95% 4%,#D61F72 0,rgba(214,31,114,.5) 26%,rgba(43,20,82,0) 60%),radial-gradient(circle at 0 100%,rgba(233,71,42,.55) 0,rgba(43,20,82,0) 48%),#2B1452;position:relative}}
.top{{position:absolute;top:60px;left:36px;display:flex;align-items:center;gap:8px;font-weight:800;font-size:16px}}.top img{{width:30px;height:30px;border-radius:8px}}
.sc{{position:absolute;inset:0;padding:240px 36px 0;opacity:0}}
.h{{font-weight:800;font-size:46px;line-height:1.04;letter-spacing:-1px}}.h span{{color:#FF8FB1}}
.chat{{margin-top:28px;background:#E7DED6;border-radius:22px;padding:18px;display:flex;flex-direction:column;gap:10px}}
.b{{max-width:85%;border-radius:14px;padding:10px 14px;font-size:18px;font-weight:600;color:#1f1f1f;background:#fff;opacity:0;transform:translateY(14px)}}
.b.me{{align-self:flex-end;background:#D9FDD3}}
.audio{{display:flex;align-items:center;gap:10px}}.audio i{{width:24px;height:24px;border-radius:50%;background:#2B1452}}.wave{{flex:1;height:6px;border-radius:5px;background:repeating-linear-gradient(90deg,#8a8a8a 0 4px,transparent 4px 8px)}}.t{{font-size:14px;color:#666}}
.ord{{background:#fff;color:#2B1452;border-radius:18px;padding:16px 18px;margin-top:14px;opacity:0;transform:translateY(14px)}}.ord b{{display:block;font-size:19px}}.ord span{{font-size:16px}}.ok{{display:inline-block;margin-top:6px;background:#e4f7ec;color:#1a7a44;border-radius:99px;padding:2px 10px;font-size:14px;font-weight:600}}
.cta{{margin-top:30px;background:#fff;color:#2B1452;border-radius:99px;text-align:center;font-weight:800;font-size:22px;padding:16px}}
.sm{{font-size:20px;line-height:1.35;margin-top:16px;color:#F1ECF4;font-weight:600}}
@keyframes in{{to{{opacity:1;transform:none}}}}@keyframes show{{0%{{opacity:0}}6%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}@keyframes stay{{0%{{opacity:0}}10%{{opacity:1}}100%{{opacity:1}}}}
"""
def html(scenes):
    out=[]; t=0
    for i,(dur,body) in enumerate(scenes):
        anim='stay' if i==len(scenes)-1 else 'show'
        out.append(f'<div class=sc style="animation:{anim} {dur}s linear {t}s forwards">{body.replace("D+",str(t)+"+")}</div>'); t+=dur
    return f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=top><img src="{ICON}">Palma Ecommerce</div>{"".join(out)}</body></html>',t
def d(base,x): return f'style="animation:in .35s ease-out {base+x:.2f}s forwards"'
async def rec(name,scenes):
    h,total=html(scenes); open(name+'.html','w').write(h)
    async with async_playwright() as p:
        b=await p.chromium.launch(); ctx=await b.new_context(viewport={'width':W,'height':H},record_video_dir='vid',record_video_size={'width':W,'height':H},device_scale_factor=1)
        pg=await ctx.new_page(); await pg.goto('file://'+os.path.abspath(name+'.html')); await pg.wait_for_timeout(int(total*1000)+600)
        v=await pg.video.path(); await ctx.close(); await b.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','0.25','-i',v,'-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-t',str(total),
      '-vf','scale=1080:1920:flags=lanczos,fps=30','-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-crf','20','-c:a','aac','-shortest','-movflags','+faststart',name+'.mp4'],check=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(total-0.5),'-i',name+'.mp4','-frames:v','1',name+'-portada.jpg'],check=True)
    os.remove(v)
