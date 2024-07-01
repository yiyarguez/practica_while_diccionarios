"""
Ejercicio 2: Factorial de un Número
Enunciado:
Escribe un programa que calcule el factorial de un número n ingresado por el usuario. El factorial de n (denotado como n!) es el producto de todos los números enteros positivos menores o iguales a n.

Procedimiento:
Solicita al usuario que ingrese un número entero n.
Inicializa una variable factorial en 1.
Usa un bucle while para iterar desde n hasta 1.
En cada iteración, multiplica la variable factorial por el valor actual de n.
Reduce el valor de n en 1.
Muestra el resultado final.

Juego de Pruebas:
Entrada: n = 5
Salida esperada: 120 (5! = 54321 = 120)
Entrada: n = 0
Salida esperada: 1 (0! = 1)
Entrada: n = 3
Salida esperada: 6 (3! = 321 = 6)

"""

def factorial_numero():
    factorial = 1

    numero = int(input("Ingresa un número: "))

    while numero > 1:
        factorial *= numero
        numero -= 1
    
    print(factorial)

factorial_numero()





