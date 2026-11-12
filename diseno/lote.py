import asyncio
from gen2 import render
P='style="color:#FF8FB1"'
def cover(kick,h,extra=''): return ("dark",f'<div style="margin-top:70px" class=k>{kick}</div><div class=h style="font-size:100px;margin-top:30px">{h}</div>{extra}')
def num(n,dark,h,body):
    c=' style="margin-top:110px;color:#FF8FB1"' if dark else ' style="margin-top:110px"'
    return ("dark" if dark else "light", f'<div class=n{c}>{n}</div><div class=h style="font-size:78px;margin-top:10px">{h}</div>{body}')
def card(t,dark=False): return f'<div class="card sub" style="margin-top:50px">{t}</div>' if not dark else f'<div class=sub style="margin-top:40px;color:#F1ECF4">{t}</div>'
def cta(h,t): return ("dark",f'<div class=h style="font-size:94px;margin-top:150px">{h}</div><div class=sub style="margin-top:40px;color:#F1ECF4">{t}</div><div class=sub style="margin-top:44px;font-size:36px;color:#FFB3C7">Partner certificado de Tiendanube</div>')
def chk(*xs): return '<div class=chk>'+''.join(f'<div><i></i>{x}</div>' for x in xs)+'</div>'
def chat(*bs): return '<div class=chat style="margin-top:44px">'+''.join(f'<div class="b{" me" if m else ""}"{" style=opacity:.5" if f else ""}>{t}</div>' for t,m,f in bs)+'</div>'
W="Escribinos al 11 6791-5562"
L={}
L['c05v2']=[
 (*cover("GUARDALO PARA REVISAR LA TUYA",f'5 errores que hacen que <span {P}>tu tienda no venda</span>'),"Deslizá y fijate cuántos tenés"),
 (*num(1,False,'Fotos <span>oscuras o borrosas</span>',card("La foto es lo único que el cliente puede tocar. Luz natural de ventana y fondo liso.")),"2: el que más ventas frena"),
 (*num(2,False,'Productos <span>sin precio</span>',chat(("precio?",0,0),("hola, precio??",0,0),("(no volvió a escribir)",0,1))),"3: la duda que frena la compra"),
 (*num(3,True,f'Sin talles <span {P}>ni medidas</span>',card("Si no sabe si le va, no compra. Poné una tabla de talles o medidas en cada producto.",True)),"4: la sorpresa en el pago"),
 (*num(4,False,'Envío <span>poco claro</span>',card("Decí cuánto cuesta y cuánto tarda antes de que llegue al pago. Las sorpresas en el último paso hacen que abandone.")),"5: el más fácil de arreglar"),
 (*num(5,False,'Nadie <span>responde</span>',card("Botón de WhatsApp visible y respuestas rápidas para las preguntas de siempre.")),"¿Querés que revisemos la tuya?"),
 (*cta(f'¿Querés que revisemos <span {P}>tu tienda?</span>',"Te decimos qué mejorar primero. Gratis y sin compromiso."),W)]
L['c06v2']=[
 (*cover("PRECIOS CLAROS, SIN COMISIÓN",f'¿Cuánto cuesta tener <span {P}>tu tienda armada?</span>'),"Deslizá: arrancamos por el más simple"),
 ("light",'<div class=k style="margin-top:130px;background:#2B1452">INICIAL · TIENDA LISTA</div><div class=h style="font-size:120px;margin-top:30px">$350.000</div><div class=sub style="margin-top:6px">de armado + $65.000 por mes</div>'+card("Tu tienda armada y con todos los productos cargados."),"Si además querés publicidad"),
 ("dark",'<div class=k style="margin-top:130px;background:#D61F72">MEDIO · EL QUE RECOMENDAMOS</div><div class=h style="font-size:120px;margin-top:30px;color:#FF8FB1">$590.000</div><div class=sub style="margin-top:6px;color:#F1ECF4">de armado + $330.000 por mes</div>'+card("Tu tienda armada y cargada, más publicidad en Instagram y Facebook para que te compren.",True),"Y si querés que hagamos todo"),
 ("light",'<div class=k style="margin-top:130px;background:#2B1452">PREMIUM · TODO HECHO</div><div class=h style="font-size:120px;margin-top:30px">$890.000</div><div class=sub style="margin-top:6px">de armado + $620.000 por mes</div>'+card("Tienda, publicidad, email y WhatsApp: todo a cargo nuestro."),"Lo que tenés que saber"),
 ("light",'<div class=h style="font-size:80px;margin-top:150px">Para que <span>tengas en cuenta</span></div>'+chk("Sin comisión sobre tus ventas","Pagás 50% al arrancar y 50% al ver tu tienda","La publicidad la pagás aparte, directo a Meta"),"¿Cuál te conviene?"),
 (*cta(f'¿Cuál <span {P}>te conviene?</span>',"Escribinos, contanos cómo vendés hoy y te recomendamos uno. Precios de lanzamiento de noviembre de 2026."),W)]
L['c07v2']=[
 (*cover("LA PREGUNTA QUE TODOS SE HACEN",f'¿Y si pago <span {P}>y no me hacen nada?</span>'),"Deslizá: por eso hay 2 garantías"),
 (*num(1,False,'Garantía <span>de la tienda</span>',card("Pagás el 50% para arrancar. Si cuando la ves no te gusta, no pagás el 50% restante.")),"2: la de la publicidad"),
 (*num(2,True,f'Garantía <span {P}>de la publicidad</span>',card("Si en 10 días hábiles tus campañas no están publicadas, ese mes no lo pagás.",True)),"Y algo más importante"),
 ("light",'<div class=h style="font-size:84px;margin-top:150px">Todo queda <span>a tu nombre</span></div>'+chk("La tienda es tuya","Las cuentas son tuyas","Tus clientes son tuyos"),"¿Te quedó alguna duda?"),
 (*cta(f'Desconfiar <span {P}>está bien</span>',"Preguntanos todo lo que necesites antes de decidir. Te respondemos por WhatsApp."),W)]
L['c09v2']=[
 (*cover("ASÍ FUNCIONA",f'Publicidad que te <span {P}>llena el WhatsApp</span>',chat(("Hola! Vi tu anuncio, ¿hacen envíos?",0,0),("Hola, quiero info por mayor",0,0))),"Deslizá: 4 pasos"),
 (*num(1,False,'Armamos <span>el anuncio</span>',card("Con tus fotos y videos, pensado para tu rubro y para tu zona o todo el país.")),"2: la gente te escribe"),
 (*num(2,False,'Te escriben <span>directo</span>',card("El anuncio abre un chat con tu WhatsApp. Sin formularios, sin vueltas.")),"3: vos vendés"),
 (*num(3,True,f'Vos <span {P}>vendés</span>',card("Respondés como siempre, o te dejamos respuestas rápidas listas para las preguntas de siempre.",True)),"4: sabés cuánto rindió"),
 (*num(4,False,'Medimos <span>todo</span>',chk("Cuánto invertiste","Cuántos te escribieron","Cuánto vendiste")),"¿Querés más mensajes?"),
 (*cta(f'¿Querés que te escriban <span {P}>más clientes?</span>',"Te contamos cómo sería la publicidad para tu marca."),W)]
L['c10v2']=[
 (*cover("MIENTRAS DORMÍS",f'Son las 2 de la mañana y <span {P}>alguien quiere comprarte</span>',chat(("Hola, ¿tenés el conjunto negro en M?",0,0),("(02:14)",0,1))),"Deslizá: qué pasa con y sin tienda"),
 ("light",'<div class=k style="margin-top:110px;background:#2B1452">SIN TIENDA</div><div class=h style="font-size:80px;margin-top:30px">A la mañana <span>ya le compró a otro</span></div>'+card("Te escribió, no le contestaste a tiempo y siguió buscando."),"Ahora mirá con tienda"),
 ("dark",f'<div class=k style="margin-top:110px;background:#D61F72">CON TIENDA</div><div class=h style="font-size:80px;margin-top:30px">Te despertás <span {P}>con la venta hecha</span></div>'+'<div class=card style="margin-top:46px;font-size:34px;line-height:1.45;color:#2B1452"><b style="font-size:38px">Pedido #3108 · 02:16</b><br>1 conjunto negro · talle M<br><span style="display:inline-block;margin-top:10px;background:#e4f7ec;color:#1a7a44;border-radius:99px;padding:6px 20px;font-size:28px;font-weight:600">Pagado</span></div>',"¿Y el WhatsApp?"),
 ("light",'<div class=h style="font-size:84px;margin-top:150px">No dejás <span>tu WhatsApp</span></div>'+card("Tus clientes te siguen escribiendo. Pero el que quiere comprar ya, compra solo."),"¿Arrancamos?"),
 (*cta(f'Tu tienda <span {P}>no duerme</span>',"Te la armamos y te cargamos todos los productos."),W)]
L['c11v2']=[
 (*cover("PENSALO UN SEGUNDO",f'Si mañana te bloquean Instagram, <span {P}>¿dónde quedan tus clientes?</span>'),"Deslizá"),
 ("light",'<div class=h style="font-size:84px;margin-top:150px">Instagram <span>no es tuyo</span></div>'+card("Una cuenta se puede bloquear o hackear de un día para el otro. Y con ella, tus contactos."),"Lo que sí es tuyo"),
 ("dark",f'<div class=h style="font-size:84px;margin-top:150px">Tu tienda <span {P}>sí es tuya</span></div>'+chk("Tus productos","Tus ventas","La lista de todos tus clientes"),"Lo ideal"),
 ("light",'<div class=h style="font-size:84px;margin-top:150px">Lo ideal: <span>las dos cosas</span></div>'+card("Instagram para que te conozcan. La tienda para venderles y no perderlos nunca."),"¿Armamos la tuya?"),
 (*cta(f'Cuidá <span {P}>a tus clientes</span>',"Te armamos la tienda donde quedan guardados, con todos tus productos."),W)]
import sys
from c04 import S as S04
from c08 import S as S08
L['c04v2']=S04
async def main():
    for k,v in L.items(): await render(v,k)
asyncio.run(main())
