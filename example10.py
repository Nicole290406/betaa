import os 
from random import randint 


i = 1
respuesta = "s"
while respuesta == "s" :
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"Lanzamiento {i}: ")
    print(f"Dice 1: {d1}")
    print(f"Dice 2: {d2}")
    print("\n")


    respuesta=input("¿Quieres volver a lanzar?(s/S/n/N): ")
    if respuesta == 'n' or 'N':
    i += 1

print(f"\nSe realizaron un total de {i - 1} lanzamientos.")