# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2018/1/24 下午8:59
# @file    : douban_top250.py
# @desc    : 抓取豆瓣电影top250链接和影片名字
#

import requests
from bs4 import BeautifulSoup


info_list = []
top250_url = 'https://movie.douban.com/top250?start={}&filter='

def save(data_list):
    # 将抓取到的信息存成文件
    print(data_list)
    with open('doubafilm_top250.txt', 'w') as f:
        for data in data_list:
            f.write(data)


def get_info():
    # 解析豆瓣电影网页
    for i in range(10):
        start = i * 25
        web_data = requests.get(top250_url.format(start))
        soup = BeautifulSoup(web_data.text, 'lxml')
        all_items = soup.find_all(class_='item')
        # print(all_items)
        for item in all_items:
            pic_div = item.find(class_='pic')
            # print(pic_div)
            item_href = pic_div.find('a')['href']
            # print(item_href)
            info_list.append(item_href)
            item_name = pic_div.find('img')['alt']
            # print(item_name)
            info_list.append(item_name)
            info_list.append('\n')
    # print(info_list)

def main():
    get_info()
    save(info_list)


if __name__ == '__main__':
    main()