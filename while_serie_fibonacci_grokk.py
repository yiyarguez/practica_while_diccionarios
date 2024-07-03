"""
Ejercicio 3: Serie de Fibonacci
Enunciado:
Escribe un programa que genere los primeros n números de la serie de Fibonacci. La serie de Fibonacci comienza con 0 y 1, y cada número siguiente es la suma de los dos anteriores.

Procedimiento:
Solicita al usuario que ingrese un número entero n.
Inicializa dos variables, a y b, con los valores 0 y 1 respectivamente.
Usa un bucle while para iterar n veces.
En cada iteración, muestra el valor de a.
Actualiza los valores de a y b de tal manera que a tome el valor de b y b tome el valor de a + b.
Muestra los valores generados.

Leonardo De Pisa (Fibonacci) -> 1,1,2,3,5,8,13,21,34,55,89,144,233,377      
Nota: Verificar si la serie de fibonaccio inicia con 0, para este ejemplo tomaremos que si inicia con 0

Juego de Pruebas:
Entrada: n = 5
Salida esperada: 0, 1, 1, 2, 3
Entrada: n = 8
Salida esperada: 0, 1, 1, 2, 3, 5, 8, 13
Entrada: n = 1
Salida esperada: 0

"""
def fibonacci():
    numero = int(input("Ingresa un numero: "))
    a = 0
    b = 1
    
    print(a)
    while numero > 1: 
        temp_a = a
        a = b 
        b = temp_a + b 
        print(a)
        
        numero -= 1

fibonacci()



"""
Ejemplo:
numero = 5

numero    temp_a        a         b        print(a)    
   5         0          1         1            1
   4         1          1         2            1
   3         1          2         3            2
   2         2          3         5            3

"""