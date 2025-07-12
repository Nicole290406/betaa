'''
Generar una lista de números teniendo en cuenta un número de inicio (li) y un número 
de fin (ls)

Los números deben ser ingresados por el usuario

Si el primer número es mayor que el segundo, la lista se debe imprimir en orden descendente

'''

import os

os.system('clear')

li = int(input("Ingresa límite inferior: "))
ls = int(input("Ingresa límite superior: "))

i = li
while i <= ls:
    print(i)
    i += 1