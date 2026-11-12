import asyncio
from gen2 import render
S=[
 ("dark", '''<div style="margin-top:70px" class=k>SIN QUE CARGUES NI UN PRODUCTO</div>
 <div class=h style="font-size:108px;margin-top:30px">Así armamos tu tienda <span style="color:#FF8FB1">en 4 pasos</span></div>
 <div class=steps><div class=st><b>1</b>Charla</div><div class=st><b>2</b>Fotos</div><div class=st><b>3</b>Armado</div><div class=st><b>4</b>Aprobás</div></div>''',
  "Paso 1: arranca gratis"),
 ("light", '''<div class=n style="margin-top:110px">1</div>
 <div class=h style="font-size:82px;margin-top:10px">Diagnóstico <span>gratis</span></div>
 <div class=chat style="margin-top:44px"><div class=b>Hola, vendo ropa por mayor en Flores</div><div class="b me">Genial. ¿Hoy cómo te hacen los pedidos?</div><div class=b>Por WhatsApp, todo el día</div></div>''',
  "Paso 2: lo único que hacés vos"),
 ("light", '''<div class=n style="margin-top:110px">2</div>
 <div class=h style="font-size:82px;margin-top:10px">Nos pasás <span>el material</span></div>
 <div class=chk><div><i></i>Fotos de tus productos</div><div><i></i>Precios y talles</div><div><i></i>Cómo cobrás y cómo enviás</div></div>''',
  "Paso 3: la parte pesada es nuestra"),
 ("dark", '''<div class=n style="margin-top:110px;color:#FF8FB1">3</div>
 <div class=h style="font-size:80px;margin-top:10px">Armamos y <span style="color:#FF8FB1">cargamos todo</span></div>
 <div class=grid><div class=tile><div class=im></div><div class=l1></div><div class=pr>$ 12.500</div></div><div class=tile><div class=im></div><div class=l1></div><div class=pr>$ 9.800</div></div><div class=tile><div class=im></div><div class=l1></div><div class=pr>$ 15.200</div></div><div class=tile><div class=im></div><div class=l1></div><div class=pr>$ 7.400</div></div></div>''',
  "Paso 4: y acá viene la garantía"),
 ("light", '''<div class=n style="margin-top:110px">4</div>
 <div class=h style="font-size:82px;margin-top:10px">La ves <span>y la aprobás</span></div>
 <div class="card sub" style="margin-top:50px">Si no te gusta, no pagás el 50% restante. Recién cuando la aprobás, sale online.</div>''',
  "¿Arrancamos con el paso 1?"),
 ("dark", '''<div class=h style="font-size:100px;margin-top:150px">¿Arrancamos con el <span style="color:#FF8FB1">paso 1?</span></div>
 <div class=sub style="margin-top:40px;color:#F1ECF4">Escribinos y te hacemos el diagnóstico gratis. Vos nos pasás fotos y precios; del resto nos encargamos nosotros.</div>
 <div class=sub style="margin-top:44px;font-size:36px;color:#FFB3C7">Partner certificado de Tiendanube</div>''',
  "Escribinos al 11 6791-5562"),
]
print(asyncio.run(render(S,'c03v2')))
