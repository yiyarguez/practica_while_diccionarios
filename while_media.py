"""
Crear un programa que calcule el promedio de una colección de valores
ingresados por el usuario. El usuario ingresará 0 como un valor centinela
para indicar que no se proporcionarán más valores. Tu programa debe
mostrar un mensaje de error apropiado si el primer valor ingresado por
el usuario es 0. Puesto que el 0 es el valor de salida, no debe
incorporarse al cálculo de la media.
"""
entrada_usuario = None
lista_de_numeros = []
promedio = 0
total = 0

while True:
    entrada_usuario = int(input("Ingresa un número: "))
    if entrada_usuario == 0:
        print("Ingresaste el número 0, este programa terminó")
        break
    try:
        lista_de_numeros.append(entrada_usuario)           
    except ValueError:
        print("Ingresa un número válido")

for numero in lista_de_numeros: 
    total += numero
promedio = total / len(lista_de_numeros)
print(f"El promedio es:{promedio:.2f}")   

