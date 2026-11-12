import asyncio
from reel import rec, d
A='<div class="b audio" {}><i></i><div class=wave></div><span class=t>{}</span></div>'
def esc1(hook):
    return (3.2, f'''<div class=h>{hook}</div><div class=chat>{A.format(d(0,.6),"0:47")}<div class=b {d(0,1.1)}>precio x mayor?? 🙏</div>{A.format(d(0,1.6),"2:05")}<div class=b {d(0,2.1)}>hola info</div></div>''')
esc2=(3.0, f'''<div class=h>Con tu tienda, el pedido <span>llega armado</span></div>
<div class=ord {d(3.2,.5)}><b>Pedido #1024 · Revendedora de Córdoba</b><span>12 jeans · talles surtidos</span><br><span class=ok>Seña recibida</span></div>
<div class=ord {d(3.2,1.1)}><b>Pedido #1025 · Local de Rosario</b><span>24 remeras · 3 colores</span><br><span class=ok>Pagado</span></div>''')
esc3=(3.0, f'''<div class=h>Te la armamos y <span>cargamos todo</span></div><div class=sm>Partner certificado de Tiendanube.<br>Diagnóstico gratis por WhatsApp.</div><div class=cta>WhatsApp 11 6791-5562</div>''')
asyncio.run(rec('reel01-A',[esc1('¿Seguís tomando pedidos <span>por audio?</span>'),esc2,esc3]))
asyncio.run(rec('reel01-B',[esc1('Si tu WhatsApp se ve así, <span>perdés ventas</span>'),esc2,esc3]))
