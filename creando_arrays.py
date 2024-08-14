import numpy as np

lista = np.arange(0,10) #Crea un array de 0 a 9
print(lista)

lista = np.arange(0,20) #Crea un array de 0 a 19
print(lista)

lista = np.arange(0,20,step=2) #step indica que va de dos en dos
print(lista)

lista = np.zeros(3) #Crea un array de 3 0, se usa para crear arreglos de 0.
print(lista)

#Creando un array de 10 x 10
array = np.zeros((10,10)) #Crea un array de 10 x 10
print(array)

#Creando un array de 10 x 5 de unos
array = np.ones((10,5)) #10 filas y 5 columnas
print(array)

#np.linspace: Es para tener una lista de datos igualmente espaciados.
#El primer parametro es con el valor que se quiere que inicie.
#El segundo parametro es con el valor que se quiere que termine.
#El tercer parametro es cuantos datos quiero generar.
lista = np.linspace(0,10,10) 
print(lista)

lista = np.linspace(0,10,100) 
print(lista)

#np.eye #Proporciona una manera rapida de crear matrices de identidad, es decir, matrices con unos en la diagonal principal.
lista = np.eye(5)
print(lista)

#np.random Genera numeros aleatorios.
lista = np.random.rand()
print(lista)

lista = np.random.rand(4) #Genera un array de una dimension pero con cuatro valores aleatorios.
print(lista)

lista = np.random.rand(4,5) #Genera un array de dos dimensiones pero con valores aleatorios. 5 Columnas y 4 Filas.
print(lista)

#np.randint: Numero aleatorio 
lista = np.random.randint(1,15) #Genera un numero aleatorio entre 1 y 15
print(lista)

lista = np.random.randint(1,100,(10,10)) #Genera un array de 10 x 10 con valores aleatorios entre 1 y 100
print(lista)
