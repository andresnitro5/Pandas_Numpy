import numpy as np

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

arr = np.array(lista)  #Se define un arreglo

print(arr.dtype)

#Creacion de matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz) #Se crea un arreglo de 3 * 3 a partir de una matriz
print(matriz)

#####IndexIn
#Listas 

print(arr[0]) #Imprime la primera posicion de la lista que es el numero 1
print(arr[1])

print(arr[0] + arr[4]) #Se suman el primero y quinto elemento de la lista algebraicamente

print(arr[:5]) #Imprime hasta la quinta posicion

print(arr[3:]) #Imprime desde la tercera posicion sin contar la tercera 

print(arr[:]) #Imprime todo el arreglo

print(arr[::2]) #Imprime todo pero de 2 en 2

print(arr[-1]) #Imprime el ultimo elemento

print(arr[-3:]) #Imprime los ultimos tres valores


###Matrices
print(matriz[0]) #Imprime la primera fila de la matriz
print(matriz[1])
print(matriz[2])

print(matriz[0,0]) #Se accede al elemento de la primera fila y primera columna
print(matriz[1,2],) #Elemento de la segunda fila y segunda columna

print(matriz[:,0]) #Se accede a la primera columna de la matriz
print(matriz[:,1])
print(matriz[:,2])

print(matriz[1:]) #Imprime la segunda y tercera fila de la matriz

print(matriz[1:,0:2]) #Imprime la segunda y tercera fila pero solo los elementos de las primeras dos columnas
print(matriz[1:,1:]) #Imprime la segunda y tercera fila pero desde solo los elementos de las ultimas dos columnas

print(matriz[2,1:]) #Imprime la tercera columna pero solo los elementos de la segunda y tercera columna