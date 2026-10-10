print("P: para modaliad presencial -> 60$")
print("O: para modalidad online -> 50$")
print("G: para modaliad clases grabadas -> 30$")
modalidad = input("Escriba la modaliad que desea: ")

if modalidad.lower() == "p":
    precio = 60
else:
    if modalidad.lower() == "o":
        precio = 50
    else: #se asume q la modaliad es grabada xdd
        if modalidad.lower() == "g":
            precio = 30
        else:
            print("modalidad incorrecta")
        precio = -1
if precio != -1:
    print(f"el monto a pagar es {precio}")
