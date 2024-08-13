import numpy as np

scalar = np.array(42)
print(scalar)
print(scalar.ndim) #Dimension: 0

#Una Dimension
vector = np.array([1,2,3,4])
print(vector)
print(vector.ndim) #Dimensión: 1

#Dos Dimensiones
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
print(matriz.ndim) #Dimensión: 2

#Tres Dimensiones
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim) #Dimensión: 3

#Agregar O Eliminar Dimensiones
vector = np.array([1,2,3,4],ndmin=10) #Con ndmin se agregan dimensiones
print(vector)
print(vector.ndim) 

#Expandir
expand = np.expand_dims(np.array([1,2,3]),axis=0) #Se utiliza expand_dims para agregar una dimension
print(expand)
print(expand.ndim)

#Exprimir o apretar: Se utiliza para eliminar dimensiones innecesarias.
print(vector)
print(vector.ndim)
vector = np.squeeze(vector) #Se utiliza squeeze para eliminar dimensiones innecesarias   
print(vector)
print(vector.ndim)


