# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/10/9 上午12:43
# @file    : pandas_score.py
# @desc    : use pandas to statistics score
#

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 读取文本文件
name = np.loadtxt('name.txt', delimiter='\n', dtype=str)
# print(name)
score1 = np.loadtxt('score1.txt', delimiter='\n', dtype=str)
score2 = np.loadtxt('score2.txt', delimiter='\n', dtype=str)
score3 = np.loadtxt('score3.txt', delimiter='\n', dtype=str)

# 将姓名与成绩封装成3个Series对象
score_series1 = Series(score1, index=name, dtype=int)
# print(score_series1)
score_series2 = Series(score2, index=name, dtype=int)
score_series3 = Series(score3, index=name, dtype=int)

print(score_series1.describe())
print(score_series2.describe())
print(score_series3.describe())

# 设定划分显示
bins = [0] + list(range(60, 101, 10))

# 统计单科在各成绩区间上的人数
cuts1 = pd.cut(score_series1, bins, right=False)
print(pd.value_counts(cuts1))
cuts2 = pd.cut(score_series2, bins, right=False)
print(pd.value_counts(cuts2))
cuts3 = pd.cut(score_series3, bins, right=False)
print(pd.value_counts(cuts3))

# print(score_series1)
# 连接各Series对象，拼接成为记录三科成绩的大表
total_score = pd.concat([score_series1, score_series2, score_series3], axis=1)
# print(total_score)
total_score.rename(columns={0: 'literature', 1: 'mathematics', 2: 'eglish'}, inplace=True)
# print(total_score)

# 划分等级
def score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# 根据三科成绩，进行函数映射，输出对应等级
total_score['literature_grade'] = total_score['literature'].map(score_to_grade)
total_score['mathematics_grade'] = total_score['mathematics'].map(score_to_grade)
total_score['eglish_grade'] = total_score['eglish'].map(score_to_grade)
# print(total_score)

# 计算单人总得分,平均分
total_score['personal_total'] = total_score.sum(axis=1)
total_score['personal_average'] = total_score['personal_total'] / 3

# 指定列顺序，重新排列
total_score = total_score.reindex(columns=['literature', 'literature_grade', 'mathematics','mathematics_grade', 'eglish', 'eglish_grade', 'personal_total', 'personal_average'])
print(total_score)

print(total_score.describe())

# 制作分级表
score_level_data = total_score.loc[:, 'literature':'eglish_grade']
# print(score_level_data)

# 设定分层索引
score_level_data.columns = [
    ['literature', 'literature', 'mathematics', 'mathematics', 'eglish', 'eglish'],
    ['score', 'grade', 'score', 'grade','score', 'grade']
]

# print(score_level_data)

# 添加单人总分，平均分
score_level_data['personal_total'] = score_level_data.sum(axis=1)
score_level_data['personal_average'] = score_level_data['personal_total'] / 3

score_level_data = score_level_data.sort_values(by='personal_total', ascending=False)

print(score_level_data)
print(score_level_data.describe())

score_level_data.to_csv('score_level_data.csv')