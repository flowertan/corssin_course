# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/8/27 22:20
# @file    : douban1.py
# @desc    : 从豆瓣获取某一部电影的海报并将海报存到本地
#

import requests, json
import os
import urllib.request

url = "https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a"

req = requests.get(url)
content = req.json()
# print(content)
img_url = content['image']
file_name = content['alt_title']
file_name = file_name.split(' ')[0]
print(file_name)

try:
    if not os.path.exists('./img'):
        os.makedirs('./img')
    # 获取文件后缀名
    file_suffix = os.path.splitext(img_url)[1]
    print(file_suffix)
    # 获取文件名，包含路径
    filename = './img%s%s%s' % (os.sep, file_name, file_suffix)
    print(filename)
    urllib.request.urlretrieve(img_url, filename=filename)

except IOError as e:
    print('IOError')

except Exception as e:
    print('Exception')
