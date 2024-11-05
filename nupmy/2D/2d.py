import numpy as np

a2d = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a2d)

dim = A.ndim  # 2
shape = A.shape  # (3,3)
#     0  1  2
#  0 |11 12 13|
#  1 |21 22 23|
#  2 |31 31 33|

# La esquina superior izquierda representa el "origen (0, 0)"
# Para acceder al 22 se debe usar [1,1] | para el 11 es [0, 0]
size = A.size  # 9
# 3 x 3
print(f'dim es: {dim}\nshape es {shape}\nsize es {size}')

print(A[0:2, 2])
# selecciona la columna
