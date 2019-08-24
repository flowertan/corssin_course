# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/8/24 19:12
# @file    : weather.py
# @desc    : 输入城市，查询当天天气
#

import requests, json


def main():
    while True:
        city = input('请输入城市，回车退出：')
        if city == '':
            break
        try:
            info = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
        except:
            print('获取错误')
        else:
            content = info.json()
            city = content['data']['city']
            print(city)
            forecast = content['data']['forecast']
            day = forecast[0]['date']
            print(day)
            high = forecast[0]['high']
            print(high)
            low = forecast[0]['low']
            print(low)
            condition = forecast[0]['type']
            print(condition)
            # print(content['data'])


if __name__ == '__main__':
    main()