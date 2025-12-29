#CAMBIOS
#Creando funciones para cada alimento/bebida
def comida ():
    comidaLista = ["Hamburguesa Clasica", "Tacos", "Enchiladas Suizas", "Ensaldada de Pollo", "Pasta Alfredo", "Club Sandwich", "Sopa Azteca", "Salmon a la Plancha", "Boneless de Pollo" ]
    comidaPrecios = [170,100,130,125,140,130,85,280,150]
    pedidosComida = [] #Para ir acumulando los alimentos si se desean agregar mas
    totalComida = 0 #Para sumar el total de aliimentos
    respuestaComida=1
    while respuestaComida==1:
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
        comidaIndice= int(comida)-1
        comidaPrecio=int(comida)-1

        nombrePlato = comidaLista[comidaIndice]
        pedidosComida.append(nombrePlato)
        totalComida += comidaPrecios[comidaIndice]
        respuestaComida=int(input("Deseas seleccionar algo mas? 1.Si / 2.No"))
    print("\n" + "==========")
    print("RESUMEN COMIDA: ")
    for platillo in pedidosComida:
        print("--", {platillo})
    print("TOTAL A PAGAR --> $", {totalComida})
    return pedidosComida, totalComida

def bebidas ():
    bebidasLista = ["Refresco", "Cerveza", "Vino", "Agua"]
    bebidasPrecios = [30,80,100,20]
    pedidosBebidas =[]
    totalBebidas =0
    respuestaBebida =1
    while respuestaBebida==1:
        print("A continuacion se muestran los bebidas disponibles")
        print("1. Refresco--->$30")
        print("2. Cerveza--->$80")
        print("3. Vino--->$100")
        print("4. Agua--->$20")
        bebida = int(input("Selecciona una opcion: "))
        bebidaIndice = int(bebida)-1
        bebidaPrecio = int(bebida)-1
        #pidiendo orden
        nombreBebida= bebidasLista[bebidaIndice]
        pedidosBebidas.append(nombreBebida)
        totalBebidas+= bebidasPrecios[bebidaIndice]
        respuestaBebida=int(input("Deseas seleccionar algo mas? 1.Si / 2.No"))
    print("\n" + "==========")
    print("RESUMEN COMIDA: ")
    for bebida in pedidosBebidas:
        print("--", {bebida})
    print("TOTAL A PAGAR -->$", {totalBebidas})
    return pedidosBebidas, totalBebidas
listaComida, costoComida = comida ()
listaBebida, costoBebida = bebidas ()
pedidoCompleto = listaBebida + listaComida
total = costoBebida + costoComida
print("----------")
print("TICKET DE COMPRA")
for productos in pedidoCompleto:
    print("--", {productos})
print("TOTAL A PAGAR $", {total})
