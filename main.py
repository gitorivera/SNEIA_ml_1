import numpy as np

# 
# a =5
# print(type(a))

# - lista con enteros usando la fincccón rnge
int_list = list(range(10))
print(int_list)

# - armar una lista de caracteres iterando sobre una lista
str_list= [str(i) for i in int_list]
print(str_list)
new_list = str_list*2
# notese que al multiplica el vector x 2 solamente se conectan dos vectores iguales
print(new_list)

int_array = np.array(int_list)
print(int_array)
new_array = int_array*2
print(new_array)

# Adicionalmente el metodeo numpy trae:
# ndim: el numero de dimensiones
# shape: el tamaño de cada dimensión
# size: El numero total de elementos en el arreglo
# dtype: el tipo de dato en el array

