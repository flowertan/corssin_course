# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/10/8 20:38
# @file    : numpy5.py
# @desc    : math statistics and sort practice
#

# 13 - Create a 10x10 array with random values and find the minimum and maximum values (创建一个10x10的随机数组，并找出最小值和最大值)

import numpy as np

arr = np.random.randn(10, 10)
print(arr)
print(arr.max(), arr.min())

# 14 - Create a random vector of size 30 and find the mean value (创建一个有30个随机元素的数组并计算其平均值)
arr = np.random.randint(1, 10, 30, int)
print(arr)
print(arr.mean())

# 40 - Create a random vector of size 10 and sort it (创建一个有10个随机元素的数组并对其排序)
arr = np.random.randn(10)
print(arr)
arr.sort()
print(arr)

# 45 - Create random vector of size 10 and replace the maximum value by 0 (创建一个有10个随机元素的数组并将最大值修改为0)
arr = np.random.randn(10)
print(arr)
max_num = arr.max()
arr[arr == max_num] = 0
print(arr)
