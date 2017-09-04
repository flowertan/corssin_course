# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/9/4 22:31
# @file    : tushare_one.py
# @desc    : 调用tushare接口获取实时票房
#

import tushare as ts
df = ts.realtime_boxoffice()
print(df)
