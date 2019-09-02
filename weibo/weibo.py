# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/9/2 23:00
# @file    : weibo.py
# @desc    : 刷微博热门页面保存到本地
#
import requests

headers = {'cookie': 'SINAGLOBAL=7702756581157.349.1538367969291;SCF=AiMykjrfngLUnTPxWYdq9H5WavnusN3SMVPaPifs2YUXBjeJ7Vjij66yeGBslNxbChySgRB5DxrzxGLzrfWjcaQ.; SUHB=0pHAkrS5kaqNqe; UM_distinctid=16b3c5795db89f-0911e5cf30eb16-37627e04-fa000-16b3c5795dc14a; UOR=www.iqiyi.com,widget.weibo.com,www.baidu.com; ULV=1560085501556:3:1:1:5688014430631.982.1560085501543:1541428037353; Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; SUB=_2AkMqMabsf8NxqwJRmP0Uy2rlaYVzywzEieKcbVc3JRMxHRl-yj9jqkUOtRB6AbGIA3djy3JSbqqIArEmzr-SCiD8pO-Y;SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWy2yGsMBsnBSCz-OR0-PgU;TC-V5-G0=1ac1bd7677fc7b61611a0c3a9b6aa0b4545677778',
 'User-Agent': 'Mozilla / 5.0(Macintosh;IntelMacOSX10_13_3) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.132Safari / 537.36'}

url = 'https://weibo.com/a/hot/realtime'

req = requests.get(url, headers=headers)
# print(req.content)
'''
req.text 是未经过编码的，保存的时候需要添加encoding参数
req.content是经过编码的，写入的时候要以二进制写入
'''
with open('hot.html', 'wb') as f:
    f.write(req.content)