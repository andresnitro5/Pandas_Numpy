import numpy as np

arr = np.arange(0,11) #Crea un arreglo de 0 a 10
print(arr)

trozo_arr = arr[0:6] #Crea un trozo del arreglo
print(trozo_arr)

#A todo el array se le quiere remplazar los valores y dejarlos en 0
trozo_arr [:] = 0
print(trozo_arr)

#Si ahora se imprime el arreglo original, se veria que todos los valores cambiaron
print(arr) #Esto pasa porque trozo_arr depende de arr y ocupa el mismo espacio de memoria que arr.

#Comando Copy () para copiar un arreglo
#Para solucionar el anterior problema, se puede usar el comando copy()
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)

#La lista original es respetada.
print(arr) #Ahora el array se imprime como se modifico en la segunda vez.
