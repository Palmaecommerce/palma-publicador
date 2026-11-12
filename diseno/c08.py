import asyncio
from gen2 import render
S=[
 ("dark", '''<div style="margin-top:70px" class=k>LE PASA A MUCHOS MAYORISTAS</div>
 <div class=h style="font-size:100px;margin-top:30px">Tu revendedora compra una vez <span style="color:#FF8FB1">y no vuelve</span></div>
 <div class=chat style="margin-top:44px;width:800px"><div class=b>Hola! Me llevo 12 de las negras</div><div class="b me">Dale, te las preparo</div><div class=b style="opacity:.5">(nunca más escribió)</div></div>''',
  "Deslizá: así la hacés volver"),
 ("light", '''<div class=n style="margin-top:110px">1</div>
 <div class=h style="font-size:80px;margin-top:10px">Guardá <span>su contacto</span></div>
 <div class=cli><div><i class=av>L</i><p><b>Laura · Córdoba</b><span>3 compras · WhatsApp y email</span></p></div><div><i class=av>M</i><p><b>Mica · Rosario</b><span>1 compra · WhatsApp y email</span></p></div><div><i class=av>S</i><p><b>Sol · La Plata</b><span>2 compras · WhatsApp y email</span></p></div></div>''',
  "2: dale un motivo para volver"),
 ("light", '''<div class=n style="margin-top:110px">2</div>
 <div class=h style="font-size:78px;margin-top:10px">Avisale cuando <span>entra mercadería</span></div>
 <div class=chat style="margin-top:44px"><div class="b me">Hola Laura! Entraron los conjuntos nuevos. ¿Te paso el link de la tienda?</div><div class=b>Siii pasame!! 😍</div></div>''',
  "3: el empujón para la segunda compra"),
 ("dark", '''<div class=n style="margin-top:110px;color:#FF8FB1">3</div>
 <div class=h style="font-size:78px;margin-top:10px">Un cupón para <span style="color:#FF8FB1">su próximo pedido</span></div>
 <div class=cup><b>VUELVO10</b><span>10% off en tu segunda compra</span></div>''',
  "4: volvé a aparecerle"),
 ("light", '''<div class=n style="margin-top:110px">4</div>
 <div class=h style="font-size:78px;margin-top:10px">Publicidad <span>solo para tus clientes</span></div>
 <div class="card sub" style="margin-top:50px">Anuncios que ven solo quienes ya te compraron o te escribieron. Ya te conocen, así que es más fácil que vuelvan.</div>''',
  "¿Querés armar este sistema?"),
 ("dark", '''<div class=h style="font-size:92px;margin-top:150px">Tus clientes ya <span style="color:#FF8FB1">te compraron una vez</span></div>
 <div class=sub style="margin-top:40px;color:#F1ECF4">Te armamos la tienda y el sistema para que vuelvan: contactos guardados, avisos, cupones y publicidad.</div>
 <div class=sub style="margin-top:44px;font-size:36px;color:#FFB3C7">Partner certificado de Tiendanube</div>''',
  "Escribinos al 11 6791-5562"),
]
if __name__=="__main__": print(asyncio.run(render(S,"c08v2")))
