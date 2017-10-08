# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/9/22 19:46
# @file    : numpy_exersises.py
# @desc    : do exersise about numpy
#

# 1 - Import the numpy package under the name np
import numpy as np
# 2 - Print the numpy version and the configuration
print(np.__version__)
np.show_config()
# 3. Create a null vector of size 10
Z = np.zeros(10)
print(Z)
# 4 - How to find the memory size of any array
Z = np.zeros((10, 10))
print("%d bytes" % (Z.size * Z.itemsize))
# 5 - How to get the documentation of the numpy add function from the command line?
np.info(np.add)

# N = tuple([eval(i) for i in input().strip().split()])
# print(N)
# print(np.zeros(N, dtype=np.int))
# print(np.eye(3, 3, k=0))

# 9 - Create a 3x3 matrix with values ranging from 0 to 8
arr = np.arange(9)
arr.reshape(3, 3)
print(arr.reshape(3, 3))

# You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array
str = input('please input number:\n')
numbers = str.strip().split()
print(numbers)
arr = np.array(numbers)
print(arr.reshape(3,3))

# You are given two arrays ( & ) of dimensions X.
# Your task is to perform the following operations:

# Add ( + )
# Subtract ( - )
# Multiply ( * )
# Divide ( / )
# Mod ( % )
# Power ( ** )

import numpy

x, y = [eval(i) for i in input().strip().split()]
arr1 = numpy.array([input().split() for _ in range(x)], dtype=int).reshape(x, y)
arr2 = numpy.array([input().split() for _ in range(x)], dtype=int).reshape(x, y)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2)
print(arr1 % arr2)
print(arr1 ** arr2)