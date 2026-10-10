import random
import calendar

año = random.randint (1900,2026)
edad = int(input("Ingrese la edad:"))

if edad < 18:
    print("no papito, camisa azul no opina!!!!")
    if año % 2 == 0:
        print(f"el año {año} es par")


print(f"Es par el año: {año}: {año % 2==0}")
print(f"Es bisiesto el año: {año}: {calendar.isleap(año)}")

print(f"Es mayor de edad: {edad}: {edad >=18}")