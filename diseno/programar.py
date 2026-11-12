import asyncio, json, shutil, glob
from gen2 import story
P='style="color:#FF8FB1"'
WA="Escribinos por WhatsApp al 11 6791-5562 y te hacemos un diagnóstico gratis."
F="Somos Palma Ecommerce, Partner certificado de Tiendanube: armamos tiendas online llave en mano para mayoristas y marcas de Flores, Once, Avellaneda y La Salada."
C=[
 ("c04v2","2026-11-12T14:00","alcance","Vender por mayor a todo el país sin moverte de tu local","Cómo vender a revendedoras de todo el país con tu tienda online mayorista 👇\n\nTe encuentran por Instagram y Facebook, arman el pedido solas, el envío se calcula solo con el código postal y cada clienta queda guardada para volver a venderle.",
  ("SIN MOVERTE DEL LOCAL",f'Vendé a revendedoras <span {P}>de todo el país</span>',"Así llegan los pedidos de todo el país."),"#ventamayorista #tiendaonline #revendedoras #tiendanube #mayoristas"),
 ("c05v2","2026-11-12T15:00","educativo","5 errores que hacen que tu tienda online no venda","¿Tu tienda online no vende? Revisá estos 5 errores 👇 Guardalo para cuando revises la tuya.\n\n1. Fotos oscuras o borrosas. 2. Productos sin precio. 3. Sin talles ni medidas. 4. Envío poco claro. 5. Nadie responde.",
  ("GUARDALO",f'5 errores que hacen que <span {P}>tu tienda no venda</span>',"¿Cuántos tenés? Están en el post de hoy."),"#tiendaonline #ventasonline #emprendedoresargentinos #tiendanube #ecommerce"),
 ("c06v2","2026-11-12T17:00","precios","Cuánto cuesta una tienda online Tiendanube armada","¿Cuánto cuesta tener tu tienda online armada? Te mostramos los 3 planes, con precios claros y sin comisión sobre tus ventas 👇\n\nInicial $350.000 + $65.000/mes · Medio $590.000 + $330.000/mes · Premium $890.000 + $620.000/mes. La publicidad se paga aparte, directo a Meta. Precios de lanzamiento de noviembre de 2026.",
  ("PRECIOS CLAROS",f'¿Cuánto cuesta <span {P}>tu tienda armada?</span>',"Los 3 planes, sin comisión sobre tus ventas."),"#tiendanube #tiendaonline #emprendedoresargentinos #mayoristas #ecommerce"),
 ("c07v2","2026-11-12T19:00","confianza","Garantía: tienda online sin riesgo","¿Y si pago y no me hacen nada? Por eso trabajamos con 2 garantías 👇\n\nSi la tienda no te gusta, no pagás el 50% restante. Si en 10 días hábiles tus campañas no están publicadas, ese mes no se paga. Y todo queda a tu nombre.",
  ("2 GARANTÍAS",f'¿Y si pago <span {P}>y no me hacen nada?</span>',"Te contamos cómo trabajamos para que no corras riesgo."),"#tiendanube #tiendaonline #emprendedores #ecommerce #agenciadigital"),
 ("c09v2","2026-11-12T21:00","publicidad","Publicidad en Instagram y Facebook que trae mensajes a WhatsApp","Publicidad en Instagram y Facebook que te llena el WhatsApp de consultas 👇\n\nArmamos el anuncio con tus fotos, la gente te escribe directo, vos vendés y medimos cuánto invertiste y cuánto vendiste.",
  ("ASÍ FUNCIONA",f'Publicidad que te <span {P}>llena el WhatsApp</span>',"4 pasos. Están en el post."),"#publicidadenredes #metaads #whatsappbusiness #emprendedoresargentinos #tiendanube"),
 ("c10v2","2026-11-13T10:00","dolor","Tienda online que vende las 24 horas","Tu tienda online vende las 24 horas, aunque estés durmiendo 👇\n\nSin tienda, el que te escribe a la noche a la mañana ya le compró a otro. Con tienda, te despertás con la venta hecha. Y seguís atendiendo por WhatsApp como siempre.",
  ("MIENTRAS DORMÍS",f'¿Cuántas ventas <span {P}>se te van de noche?</span>',"Tu tienda puede vender las 24 horas."),"#tiendaonline #ventasonline #tiendanube #emprendedoresargentinos #ecommerce"),
 ("c11v2","2026-11-13T13:00","riesgo","Por qué tener tienda online además de Instagram","Si mañana te bloquean Instagram, ¿dónde quedan tus clientes? 👇\n\nInstagram no es tuyo: una cuenta se puede bloquear o hackear. Tu tienda online sí: tus productos, tus ventas y la lista de todos tus clientes.",
  ("PENSALO UN SEGUNDO",f'¿Y si mañana <span {P}>te bloquean Instagram?</span>',"Tus clientes tienen que estar en un lugar tuyo."),"#tiendaonline #emprendedoresargentinos #tiendanube #ventasonline #mayoristas"),
]
async def main():
    for k,*_,st,_h in [(c[0],None,None,None,None,c[5],None) for c in C]: await story(*st,k)
asyncio.run(main())
cal_p='/home/claude/palma-publicador/calendario.json'; cal=json.load(open(cal_p))
cal=[x for x in cal if not x["id"].startswith("v2-c04")]
for k,fecha,tema,seo,cuerpo,st,tags in C:
    imgs=sorted(f.split('/')[-1] for f in glob.glob(f'out/{k}-0*.jpg'))
    for f in imgs+[f'{k}-historia.jpg']: shutil.copy('out/'+f,'/home/claude/palma-publicador/media/'+f)
    texto=f"{cuerpo}\n\n{F}\n\n{WA}\n\n{tags}"
    cal.append({"id":f"v2-{k}","fecha":fecha+":00-03:00","tipo":"carrusel","tema":tema,"seo":seo,"imagenes":imgs,"texto":texto,"facebook":True,"aprobado":True})
    h=fecha[:-2]+"01"
    cal.append({"id":f"v2-{k}-historia","fecha":h+":00-03:00","tipo":"historia","tema":tema,"imagenes":[f"{k}-historia.jpg"],"aprobado":True})
json.dump(cal,open(cal_p,'w'),ensure_ascii=False,indent=2)
print(len(cal))
