# from numpy import array
# import numpy as np
# # a = array([1, 2, 3])
# # print(a)
# # b = [4,5,6]
# # print(str(b))

# # a0 = np.zeros((3, 3))
# # a1  = np.ones((2, 2))
# # ar  = np.arange(0, 10, 2)

# # print(a0)
# # print(a1)
# # print(ar)

# # arr1 = np.array([1, 2, 3])
# # arr2 = np.array([8, 4, 1])

# # arr3 = arr1 - arr2 

# # print(arr3)

# arr1 = np.array([[1,2], [3,4], [5,6]])
# arr2 = np.array([[4,1], [2,7], [6,2]])

# print(arr1)
# print(arr2)

# arr3 = arr1 + arr2 

# print(arr3)

try:
    res = 10 / 0
except ZeroDivisionError:
    res = "Infinity"
print(res)