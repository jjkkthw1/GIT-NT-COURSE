edad = int(input("Introduzca la edad: "))

if edad < 0:
    print("La edad no puede ser un valor negativo")
else:
    entrada = 10000

    if edad < 2:
        porc_descuento = 100
    elif edad <= 5:
        porc_descuento = 50
    elif edad <= 10:
        porc_descuento = 20
    elif edad <= 55:
        porc_descuento = 0
    else:
        sexo = input("Introduzca el sexo (M o F): ")
        if (sexo.upper() == "M" and edad >= 65) or (sexo.upper() == "F"):
            porc_descuento = 30
        else:
            porc_descuento = 0 

    if porc_descuento < 50:
        dia = input("Introduzca el dia: ")
        if dia.lower() == "lunes":
            porc_descuento = 50


    if porc_descuento < 30:
        estudiante = input("Es estudiante (si o no): ")
        if estudiante.lower() == "si":
            porc_descuento = 25

    if porc_descuento != 0:
        descuento = entrada * porc_descuento / 100
        print(f"El porcentaje de descuento asigando es {porc_descuento}%")
        print(f"EL monto del descuento es  {descuento}")
    else:
        descuento = 0

    monto_pagar = entrada - descuento

    print(f"El monto a pagar es {monto_pagar}")
	print("Nobody knows me Caracas, no one like  youuuu")
