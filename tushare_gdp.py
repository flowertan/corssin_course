# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/9/21 22:13
# @file    : tushare_gdp.py
# @desc    : 通过tushare接口获取年度GDP和季度GDP，并绘图
#

from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts

#获取年度GDP
years_gdp = ts.get_gdp_year()
#保存数据用来绘图
years = []
year_gdps = []

for i in range(5):
    years.append(int(years_gdp.iloc[i]['year']))
    year_gdps.append(int(years_gdp.iloc[i]['gdp']))
# print(years)
# print(year_gdps)

#get quarter GDP
quarters_gdp = ts.get_gdp_quarter()
quarters = []
quarter_gdps = []

for i in range(25):
    quarter_info = quarters_gdp.iloc[i]
    # print(quarter_info)
    #delete out of range five years
    if int(quarter_info.quarter) > years[0]:
        continue
    elif int(quarter_info.quarter) < years[-1]:
        break
    quarters.append(int(quarter_info.quarter))
    quarter_gdps.append(int(quarter_info.gdp))
#print(quarter_gdps)
# to figure
years.reverse()
year_gdps.reverse()
quarters.reverse()
quarter_gdps.reverse()

# the fourth quarter's GDP is one year, to get one quarter GDP
quarter_copy = quarter_gdps.copy()
for i in range(len(quarter_gdps)):
    if i % 4 != 0:
        quarter_gdps[i] -= quarter_copy[i-1]
plt.figure()
font = FontProperties(fname='simfang.ttf', size=10)
plt.subplot(211)
plt.bar(years, year_gdps)
plt.xticks(years)
plt.ylabel(u'年度GDP', fontproperties=font)
plt.title(u'近五年GDP比较', fontproperties=font)
plt.subplot(212)
for i in range(0, 20, 4):
    plt.plot(np.arange(1, 5), quarter_gdps[i:i+4], linestyle='dashed', marker='o', label=years[i//4])
plt.legend(loc='upper left')
plt.xticks([i for i in range(1, 5)])
plt.xlabel(u'季度', fontproperties=font)
plt.ylabel(u'单季度GDP', fontproperties=font)
plt.title(u'近五年单季度GDP走势', fontproperties=font)
plt.show()
