import numpy as np

a2d = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a2d)

# ATRIBUTOS
dim = A.ndim  # 2

shape = A.shape  # (3,3)
#     0  1  2
#  0 |11 12 13|
#  1 |21 22 23|
#  2 |31 31 33|

# La esquina superior izquierda representa el "origen (0, 0)
# Para acceder al 22 se debe usar [1,1] | para el 11 es [0, 0]

size = A.size  # 9
# 3 x 3

print(f'dim es: {dim}\nshape es {shape}\nsize es {size}')

print(A[0:2, 2])
# ### ver línea 9 ###

# [0:2] selecciona las filas 0 y 1 [11, 12, 13] y [21, 22, 23]
# [, 2] selecciona la columna 2 (13, 23)


# FUNCIONES

# OPERACIONES
# SUMAS Y RESTAS

x = np.array([1, 0], [0, 1])
y = np.array([2, 1], [1, 2])
z = x + y

# z = [[1+2, 0+1], [0+1, 1+2]]
# z= [[3, 1], [1, 3]]

# MULTIPLICACIÓN

a = np.array([2, 1], [1, 2])
b = np.array([3, 2], [2, 3])
c = 2 * a
d = a * b
# c = ([4, 2], [2, 4])
# d = ([6, 2], [2, 6])


# DOT PRODUCT

# Para que dos matrices puedan multiplicarse, el n° de columnas
# De A debe coindicir con el n° de filas de B
A = np.array([[0, 1, 1], [1, 0, 1]])
# A =
# [[0, 1, 1],
# [1, 0, 1]]
B = np.array([[1, 1], [1, 1], [-1, 1]])
# B =
# [[1, 1],
#  [1, 1],
#  [-1, 1]]

C = np.dot(A, B)
# C[0,0] = (0×1)+(1×1)+(1×−1)=0+1−1=0
# C[0,1] = (0×1)+(1×1)+(1×1)=0+1+1=2
# C[1,0] = (1×1)+(0×1)+(1×−1)=1+0−1=0
# C[1,1] = (1×1)+(0×1)+(1×1)=1+0+1=2
# c = 
# |0 2|
# |0 2|