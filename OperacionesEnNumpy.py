import numpy as np

lista = [1,2]
print(lista)
print(lista * 2) #Se repite la lista dos veces

arr = np.arange(0,11)

arr2 = arr.copy() #Se crea una copia del array

print(arr * 2) #Se multiplica cada elemento del array por 2

print(arr + 2) #Se le suma 2 a cada elemento del array

print(11 / arr) #Se divide 11 entre cada elemento del array