# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/9/17 12:38
# @file    : tuare_movie.py
# @desc    : 通过tushare获取当日top3电影，绘制电影票房走势
#

import tushare as ts
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
import datetime

today = datetime.date.today()
today_display = str(today)
month = today_display[:7]
movie = ts.month_boxoffice(month)
top_three = movie.head(3)

#save top3 movie name
movie_names = list(top_three['MovieName'])
print(movie_names)
#save boxoffeice
boxoffice_record = {}
for i in range(3):
    boxoffice_record[movie_names[i]] = []
print(boxoffice_record)

#save date in recent 7 days
date_record = []
for i in range(7):
    #将当月top3的票房的近7日票房存入之前的dic中
    current = str(today + datetime.timedelta(days=i) - datetime.timedelta(days=7))
    print(current)
    date_record.append(current)
    #get current day boxoffice
    single_day_boxoffice = ts.day_boxoffice(current)
    #print(single_day_boxoffice)
    for j in range(len(movie_names)):
        movie_boxoffice = boxoffice_record[movie_names[j]]
        top3_movie = single_day_boxoffice[single_day_boxoffice['MovieName'] == movie_names[j]]
        if top3_movie.empty:
            movie_boxoffice.append(0)
        else:
            movie_boxoffice.append(float(top3_movie['BoxOffice']))
#print(boxoffice_record)

days = np.arange(7)
boxoffices = np.array((boxoffice_record[movie_names[0]], boxoffice_record[movie_names[1]], boxoffice_record[movie_names[2]]))
print(boxoffices)

#绘图
font = FontProperties(fname='simfang.ttf', size=14)
fig = plt.figure(figsize=(10, 6))
plt.plot(days, boxoffices[0], color='black', linestyle='-', linewidth=2.5, label=movie_names[0])
plt.plot(days, boxoffices[1], color='blue', linestyle='-', linewidth=2.5, label=movie_names[1])
plt.plot(days, boxoffices[2], color='red', linestyle='-', linewidth=2.5, label=movie_names[2])
plt.legend(loc='upper left', prop=font)
plt.title('%s票房top3电影近7日走势' % month, fontproperties=font)
plt.xlabel(u'日期', fontproperties=font)
plt.ylabel(u'当日票房', fontproperties=font)
plt.xticks(days, date_record)
plt.show()