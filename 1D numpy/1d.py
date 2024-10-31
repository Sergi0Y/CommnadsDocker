import numpy as np

""" c = np.array([-10, 201, 43, 94, 502])

# max & min
max = c.max()
min = c.min()
sum = max + min
print(sum) """

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = arr1 + arr2
print(arr3)

import numpy as np

arr1 = np.array([3, 5])
arr2 = np.array([2, 4])
c = np.dot(arr1, arr2)
print(c)

""" 
# LINSPACE (inicio, fin, num = cant de elementos)
import numpy as np

# necesito un array que esté entre [-2, 2] y de 5 elementos

line = np.linspace(-2, 2, num=5)
print(line)
"""
""" 
import numpy as np
nump = np.linspace(5, 4, num=6)
# print(nump)
arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
    print(x)

import numpy as np
arr1 = [1, 2, 3, 4, 5] 
arr2 = [1, 0, 1, 0, 1]

x = np.array(arr1)
y = np.array(arr2)

z = np.multiply(x, y)
print(z)
 """
""" import numpy as np

a = [1, 2, 3]
b = [8, 9, 10]

arr1 = np.array(a)
arr2 = np.array(b)

a = np.add(arr1, arr2)
s = np.subtract(arr1, arr2)
m = np.multiply(arr1, arr2)
d = np.divide(arr1, arr2)
dot = np.dot(arr1, arr2)
print(f'La suma es: {a}\nLa resta es: {s}\nL multiplicación es: {m}\nLa división es: {d}\nEl dot es: {dot}') """


