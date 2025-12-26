#CAMBIOS
#LOS ELEMENTOS SERÁN INTRODUCIDOS A UNA LISTA PARA PODER MANEJARLO CON MAYOR FACILIDAD
comidaLista = ["Hamburguesa Clasica", "Tacos", "Enchiladas Suizas", "Ensaldada de Pollo", "Pasta Alfredo", "Club Sandwich", "Sopa Azteca", "Salmon a la Plancha", "Boneless de Pollo" ]
comidaPrecios = [170,100,130,125,140,130,85,280,150]
bebidasLista = ["Refresco", "Cerveza", "Vino", "Agua"]
bebidasPrecios = [30,80,100,20]
print("A continuacion se muestran los platillos disponibles")
print("1. Hamburguesa Clasica---> $170")
print("2. Tacos (orden de 5)---> $100 ")
print("3. Enchiladas Suizas ---> $130 ")
print("4. Ensalda de Pollo---> $125 ")
print("5. Pasta Alfredo---> $140 ")
print("6. Club Sandwich---> $130 ")
print("7. Sopa Azteca---> $85 ")
print("8. Salmon a la plancha---> $280")
print("9. Boneless de Pollo---> $150")
comida = int(input("Selecciona una opcion: "))
print("A continuacion se muestran los bebidas disponibles")
print("1. Refresco--->$30")
print("2. Cerveza--->$80")
print("3. Vino--->$100")
print("4. Agua--->$20")
bebida = int(input("Selecciona una opcion: "))
#conviertiendo el valor obtenido a valor entero
comidaIndice = int(comida)-1
bebidaIndice = int(bebida)-1
precioComida = {comidaPrecios[comidaIndice]}
precioBebida = {bebidasPrecios[bebidaIndice]}
print("Preparando ", {comidaLista[comidaIndice]}, precioComida )
print("Preparando ", {bebidasLista[bebidaIndice]}, precioBebida)


