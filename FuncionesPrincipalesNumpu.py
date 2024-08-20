import numpy as np

#Se definen numeros aleatorios del 1 al 20 en un vector.
arr = np.random.randint(1,20,10)
print(arr)

#Ahora se lleva a una estructura matricial
matriz = arr.reshape(2,5) #Dos filas y 5 columnas
print(matriz)

#Funcion max() devuelve el valor maximo de un arreglo
maximo_vector = arr.max()
print(maximo_vector)

maximo_matriz = matriz.max()
print(maximo_matriz)

#Funcion concatenacion: concatena dos vectores o matrices
#Se crea un array de dos dimensiones
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

c = np.concatenate((a,b) , axis = 0)
print(c)




