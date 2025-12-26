#CAMBIOS
#Creando funciones para cada alimento/bebida
def comida ():
    comidaLista = ["Hamburguesa Clasica", "Tacos", "Enchiladas Suizas", "Ensaldada de Pollo", "Pasta Alfredo", "Club Sandwich", "Sopa Azteca", "Salmon a la Plancha", "Boneless de Pollo" ]
    comidaPrecios = [170,100,130,125,140,130,85,280,150]
    print("A continuacion se muestran los platillos disponibles")
    while True:
    print("1. Hamburguesa Clasica---> $170")
    print("2. Tacos (orden de 5)---> $100 ")
    print("3. Enchiladas Suizas ---> $130 ")
    print("4. Ensalda de Pollo---> $125 ")
    print("5. Pasta Alfredo---> $140 ")
    print("6. Club Sandwich---> $130 ")
    print("7. Sopa Azteca---> $85 ")
    print("8. Salmon a la plancha---> $280")
    print("9. Salir")
    comida = int(input("Selecciona una opcion: "))
    comidaIndice= int(comida)-1
    comidaPrecio=int(comida)-1
    respuesta=int(input("Deseas seleccionar algo mas? 1.Si / 2.No"))
    if(respuesta==1):
        #bloque de codigo
    else:
        print("Pasando a las bebidas")
comida ()

def bebidas ():
    bebidasLista = ["Refresco", "Cerveza", "Vino", "Agua"]
    bebidasPrecios = [30,80,100,20]
    print("A continuacion se muestran los bebidas disponibles")
    print("1. Refresco--->$30")
    print("2. Cerveza--->$80")
    print("3. Vino--->$100")
    print("4. Agua--->$20")
    bebida = int(input("Selecciona una opcion: "))
    #conviertiendo el valor obtenido a valor entero
    bebidaIndice = int(bebida)-1
    bebidaPrecio = int(bebida)-1

    print("****CUENTA****")
    print("**** ", {comidaLista[comidaIndice]}, " $", {comidaPrecios[comidaPrecio]})
    print("**** ", {bebidasLista[bebidaIndice]}, " $", {bebidasPrecios[bebidaPrecio]})
menu ()
print("Deseas seleccionar algo mas? 1.Si/2.No ")
respuesta = int(input("Deseas seleccionar algo mas? 1.Si/ 2.No"))
