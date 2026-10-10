import random

edad = random.randint(-5,100)

print(f"La edad es {edad}")
if edad < 0:
    print("Edad invalida")
elif edad < edad <= 2:
    print("Es un bebe")
elif edad <= 10:
    print("Es un niño")
elif edad <= 17:
    print ("Es un adolescente")
elif edad <= 25:
    print("Es un adulto joven")
elif edad <= 55:
    print ("Es un adulto")
elif edad <= 75:
    print("Es un adulto mayor")