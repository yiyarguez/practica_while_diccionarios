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

Juego de Pruebas:
Entrada: n = 5
Salida esperada: 0, 1, 1, 2, 3
Entrada: n = 8
Salida esperada: 0, 1, 1, 2, 3, 5, 8, 13
Entrada: n = 1
Salida esperada: 0

"""