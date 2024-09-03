import numpy as np

arr = np.linspace(1 , 10, 10, dtype='int8') #Se imprime 10 elementos enteros entre 1 y 10 espaciados uniformemente.
print(arr)

indices_cont = arr > 5 #Se crea un arreglo con los elementos que sean mayor a 5
print(indices_cont)

#Ahora se va a filtrar el array con indices_cont y solo se va a imprimir los valores que sean true
print(arr[indices_cont])

#Ahora se filtra el array con los valor mayores que 5 y menores que 9.
print(arr[(arr > 5) & (arr < 9)])

#El siguiente codigo hace que los valores mayores que 5 se conviertan en 99.
arr[arr > 5] = 99
print(arr)