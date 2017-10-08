# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/10/8 19:58
# @file    : numpy3.py
# @desc    : numpy exercise
#

import numpy as np

# 25 - Given a 1D array, negate all elements which are between 3 and 8, in place. (给定一个一维数组，将元素值在3至8之间的元素置为其原本的相反数)

arr = np.arange(10)
arr[(arr >=3) & (arr <= 8)] *= -1
print(arr)

# 75 - How to swap two rows of an array? (如何交换一个数组的两行？)
arr = np.random.randn(4,4)
print(arr)
print('#####')
print(arr[[1,3]])
print('#####')
arr[[1,3]] = arr[[3,1]]
print(arr)
arr[[1,3]] = 0
print('*****')
print(arr)