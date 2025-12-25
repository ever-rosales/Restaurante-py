#Creando un restaurante
#un restaurante cuenta con comida y bebidas
print("******Bienvenido******")
print("A continuación se encuentran los platillos disponibles")
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
if (comida == 1):
    print("Preparando Hamburguesa Clasica...")
elif (comida==2):
    print("Preparando orden de tacos")
elif (comida==3):
    print("Preparando enchiladas suizas")
elif (comida==4):
    print("Preparando ensalada de pollo")
elif (comida==5):
    print("Preparando pasta Alfredo")
elif (comida==6):
    print("Preparado club sandwich")
elif (comida==7):
    print("Preparando sopa azteca")
elif (comida==8):
    print("Preparando salmon a la plancha")
elif (comida==9):
    print("Preparando boneless de pollo")
else:
    print("Selecciona una opcion correcta")

print("A continuacion se muestran las bebidas disponibles")
print("1. Refresco")
print("2. Cerveza")
print("3. Vino")
print("4. Agua")
bebida=int(input("Selecciona una opcion: "))
if(bebida==1):
    print("Preparando refresco")
elif(bebida==2):
    print("Preparando cerveza")
elif(bebida==3):
    print("Preparando vino")
elif (bebida==4):
    print("Preparando agua")
else:
    print("Selecciona una opcion valida")