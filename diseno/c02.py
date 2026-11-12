import asyncio
from gen2 import render
A='<div class="b audio"><i></i><div class=wave></div><span class=t>{}</span></div>'
S=[
 ("dark", f'''<div style="margin-top:70px" class=k>SI TE PASAN 2, ESTÁS PERDIENDO VENTAS</div>
 <div class=h style="font-size:100px;margin-top:30px">¿Seguís tomando pedidos <span style="color:#FF8FB1">por audio?</span></div>
 <div class=chat style="margin-top:50px;width:760px">{A.format("0:47")}<div class=b>Hola, precio x mayor?? 🙏</div>{A.format("2:05")}</div>''',
  "Deslizá y contá cuántas te pasan"),
 ("light", '''<div class=n style="margin-top:110px">1</div>
 <div class=h style="font-size:82px;margin-top:10px">Te pasás el día contestando <span>"¿precio?"</span></div>
 <div class=chat style="margin-top:46px"><div class=b>precio?</div><div class=b>precio del conjunto negro?</div></div>''',
  "La 2 te hace perder plata sin darte cuenta"),
 ("light", '''<div class=n style="margin-top:110px">2</div>
 <div class=h style="font-size:82px;margin-top:10px">Vendés algo que <span>ya no tenés</span></div>
 <div class="card sub" style="margin-top:50px">El stock lo llevás en un cuaderno o en la cabeza. Le confirmás a un cliente y después tenés que decirle que no hay.</div>''',
  "La 3 es la que más duele"),
 ("dark", '''<div class=n style="margin-top:110px;color:#FF8FB1">3</div>
 <div class=h style="font-size:84px;margin-top:10px">La revendedora compra una vez <span>y no vuelve</span></div>
 <div class=sub style="margin-top:44px;color:#F1ECF4">No es que no le gustó. Es que no tenés cómo volver a escribirle cuando entra mercadería nueva.</div>''',
  "Faltan 2. Seguí"),
 ("light", '''<div class=n style="margin-top:110px">4</div>
 <div class=h style="font-size:82px;margin-top:10px">Te separan mercadería <span>y no la pasan a buscar</span></div>
 <div class=chat style="margin-top:30px;gap:12px"><div class=b>Separame 12 de esas que paso el jueves</div><div class="b me">Dale, te las guardo 👍</div><div class=b style="opacity:.55">(el jueves no vino nadie)</div></div>''',
  "Última, y es la que más ventas te frena"),
 ("light", '''<div class=n style="margin-top:110px">5</div>
 <div class=h style="font-size:82px;margin-top:10px">Solo te compra <span>el que pasa por el local</span></div>
 <div class="card sub" style="margin-top:50px">Si no vienen a Flores, a La Salada o a la feria, no te compran. Y hay revendedoras en todo el país buscando lo que vendés.</div>''',
  "¿Cuántas te pasaron? Mirá esto"),
 ("dark", '''<div class=h style="font-size:100px;margin-top:150px">¿Te pasan <span>2 o más?</span></div>
 <div class=sub style="margin-top:40px;color:#F1ECF4">Tu negocio ya necesita una tienda online. Te la armamos y te cargamos todos los productos: los pedidos llegan armados, el stock se descuenta solo y cada cliente queda guardado.</div>
 <div class=sub style="margin-top:44px;font-size:36px;color:#FFB3C7">Partner certificado de Tiendanube</div>''',
  "Escribinos al 11 6791-5562"),
]
print(asyncio.run(render(S,'c02v2')))
