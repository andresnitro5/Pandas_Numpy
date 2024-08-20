import numpy as np

#Se generan numeros aleatorios entre 1 y 10.
arr = np.random.randint(1,10,(3,2))
#Se imprime la forma original del arreglo
print("Forma original: ",arr.shape) #Con shape se obtiene la forma del arreglo.
print(arr) #Arreglo de 3 filas y 2 columnas

#Ahora se cambia la forma del arreglo a (1,6)
arr_reshaped  = arr.reshape(1,6) #Con reshape se cambia la forma del arreglo
#Se imprime la nueva forma
print(arr_reshaped.shape)
print(arr_reshaped) #Arreglo de una fila y 6 columnas.
