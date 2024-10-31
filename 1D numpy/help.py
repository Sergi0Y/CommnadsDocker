import numpy as np

a = np.array([0, 2, 3, 4])
print(a[1:4:2])
# 1: DESDE DONDE SE COMIENZA
# :4: CANTIDAD DE ELEMENTOS CON LOS QUE SE QUIERE TRABAJAR
# :2 TOMA ELEMENTOS CADA 2 POSICIONES


print(a.shape)

b = np.array([10, 20, 30, 40, 50, 60, 70])
# TAMAÑO DEL ARRAY
s = b.size
# CANTIDAD DE DIMENSIONES
d = b.ndim
# FORMA (DIMENSIONES)
sh = b.shape
print(f"The size is {s}.\nThe dimension is {d}.\nThe shape is {sh}.")

# __FUNCIONES__

arr = np.array([1, 1, 1, 1])

# PROMEDIO
m = arr.mean()

# DESVIACIÓN ESTÁNDAR
dst = arr.std()

# VALOR MÁS GRANDE
max = arr.max()

# VALOR MÁS PEQUEÑO
min = arr.min()




# __OPERACIONES__

# SUMA & RESTA
import numpy as np

u = np.array([1, 0])
v = np.array([0, 1])
# IGUAL FUNCIONA z = u + v
add = np.add(u, v)
print(add)  # [1, 1]

# RESTA
sub = np.subtract(u, v)
print(sub)  # [0, -1]

# MULTIPLICACIÓN & DIVISIÓN
import numpy as np

x = np.array([1, 2])
y = np.array([2, 1])

m = np.multiply(x, y)
print(m)  # [2, 2]

# DIVISIÓN
d = np.divide(x, y)
print(d)  # [0.5, 2]

# DOT PRODUCT
"""
Es una operación matemática que se aplica a dos vectores. Consiste en multiplicar los elementos correspondientes de cada vector y luego sumar los productos obtenidos. Esta operación resulta en un único número (escalar) y es muy útil en álgebra lineal, procesamiento de señales, gráficos por computadora y aprendizaje automático."""
import numpy as np

a = np.array([1, 2])
b = np.array([3, 2])

dot = np.dot(a, b)
print(dot)  # 7

# SUMA A CADA VALOR DEL ARRAY (ADDING CONSTANT)
import numpy as np

u = np.array([1, 2, 3, -1]) 
c = u + 1
print(c)  # [2, 3, 4, 0]

# FUNCIONES MATEMÁTICAS
pi = np.pi
print(pi)  # DEVUELVE EL VALOR DE PI (3,14...)

x = np.array([0, np.pi / 2, np.pi])
y = np.sin(x)  # seno de x
print(y)


# LINSPACE (inicio, fin, num = cant de elementos)
import numpy as np

# necesito un array que esté entre [-2, 2] y de 5 elementos

l = np.linspace(-2, 2, num = 5)
print(l)

