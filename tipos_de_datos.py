import pandas as pd
import numpy as np


#arr = np.array([1,2,3,4] , dtype="float64") #Se define un array con una lista con el tipo de dato float
#print(arr)

#print(arr.dtype) #Esta propiedad sirve para obtener el tipo de dato que tiene el objeto

#arr = np.array([1,2,3,4])
#arr = arr.astype(np.float64)  #Tambien se puede cambiar el tipo de dato con la funcion np.astype

#print(arr.dtype)

#arr = np.array([0,1,2,3,4])
#arr =arr.astype(np.bool_)

#print(arr)  #El primero lo imprimira como false porque es 0 los demas como true

#arr = np.array([0,1,2,3,4])
#arr = arr.astype(np.str_)

#print(arr) #Ahora los imprime como caracteres

arr = np.array(['0','1','2','3','4'])
arr = arr.astype(np.int64) #Se pasa de String a entero
print(arr) 

