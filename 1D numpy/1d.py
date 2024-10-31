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