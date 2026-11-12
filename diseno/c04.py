import asyncio
from gen2 import render
S=[
 ("dark", '''<div style="margin-top:70px" class=k>SIN MOVERTE DEL LOCAL</div>
 <div class=h style="font-size:104px;margin-top:30px">Vendé a revendedoras <span style="color:#FF8FB1">de todo el país</span></div>
 <div class=chips><span>Córdoba</span><span>Rosario</span><span>Mendoza</span><span>Tucumán</span><span>Neuquén</span><span>Mar del Plata</span><span>Salta</span></div>''',
  "Deslizá: así llegan los pedidos"),
 ("light", '''<div class=n style="margin-top:110px">1</div>
 <div class=h style="font-size:80px;margin-top:10px">Te encuentran <span>en Instagram y Facebook</span></div>
 <div class="card sub" style="margin-top:50px">Hacemos publicidad para que te vean revendedoras de todo el país, no solo las que pasan por el local.</div>''',
  "2: compran solas, a cualquier hora"),
 ("light", '''<div class=n style="margin-top:110px">2</div>
 <div class=h style="font-size:80px;margin-top:10px">Arman el pedido <span>solas</span></div>
 <div class=card style="margin-top:46px;font-size:34px;line-height:1.45"><b style="font-size:38px">Pedido #2051 · Revendedora de Mendoza</b><br>18 prendas · talles surtidos<br><span style="display:inline-block;margin-top:10px;background:#e4f7ec;color:#1a7a44;border-radius:99px;padding:6px 20px;font-size:28px;font-weight:600">Pagado por transferencia</span></div>''',
  "3: el envío se calcula solo"),
 ("dark", '''<div class=n style="margin-top:110px;color:#FF8FB1">3</div>
 <div class=h style="font-size:80px;margin-top:10px">El envío <span style="color:#FF8FB1">se calcula solo</span></div>
 <div class=cp><div class=in>Código postal: 5500</div><div class=op><span>Correo a domicilio</span><b>Calculado</b></div><div class=op style="border:0"><span>Retiro en sucursal</span><b>Calculado</b></div></div>''',
  "4: y no la perdés más"),
 ("light", '''<div class=n style="margin-top:110px">4</div>
 <div class=h style="font-size:80px;margin-top:10px">Queda guardada <span>para volver a venderle</span></div>
 <div class="card sub" style="margin-top:50px">Nombre, WhatsApp, email y qué compró. Cuando entra mercadería nueva, le avisás.</div>''',
  "¿Querés vender a todo el país?"),
 ("dark", '''<div class=h style="font-size:96px;margin-top:150px">Tu local, <span style="color:#FF8FB1">abierto en todo el país</span></div>
 <div class=sub style="margin-top:40px;color:#F1ECF4">Te armamos la tienda con todos tus productos y la publicidad para que te encuentren. Vos despachás.</div>
 <div class=sub style="margin-top:44px;font-size:36px;color:#FFB3C7">Partner certificado de Tiendanube</div>''',
  "Escribinos al 11 6791-5562"),
]
if __name__=="__main__": print(asyncio.run(render(S,"c04v2")))
