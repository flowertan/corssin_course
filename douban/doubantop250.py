# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/8/27 22:54
# @file    : doubantop250.py
# @desc    : 从豆瓣获取排名top250的电影信息
#

import time, requests, csv, os
import urllib.request

headers = ['id', 'title', 'rate', 'casts', 'image']


def download_pic(movies):
    try:
        if not os.path.exists('./imgs'):
            os.makedirs('./imgs')

        for movie in movies:
            file_suffix = os.path.splitext(movie[-1])[1]
            # print(file_suffix)
            file_name = './imgs%s%s%s' % (os.sep, movie[1], file_suffix)
            # print(file_name)
            urllib.request.urlretrieve(movie[-1], filename=file_name)

    except IOError as e:
        print('IOError')
    except Exception as e:
        print('Exception')


def load():
    data = []
    with open('movies.csv', 'r', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            print(row)
            data.append(row)
    return data


def save(data):
    # 将输入的数据保存到CSV文件中
    with open('movies.csv', 'a+', newline='', encoding='utf-8-sig') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writerows(data)


'''
input : 要解析的网址
output: 解析出的电影信息列表，包括id,评分，电影名，主演，海报链接
'''

def get_info(url):
    # 解析从API接口拿到的数据
    movies = []
    req = requests.get(url)
    content = req.json()
    subjects = content.get('subjects')
    for subject in subjects:
        temp = {}
        # print(subject)
        temp['id'] = subject.get('id')
        temp['title'] = subject.get('title')
        rating = subject.get('rating')
        temp['rate'] = rating.get('average')
        temp['casts'] = ''
        for cast in subject.get('casts'):
            temp['casts'] += cast.get('name')
            temp['casts'] += ','
        images = subject.get('images')
        temp['image'] = images.get('large')
        # print(temp)
        movies.append(temp)
    return movies


def main():
    for i in range(0, 250, 20):
        url = 'https://api.douban.com/v2/movie/top250?start=%d&apikey=0df993c66c0c636e29ecbb5344252a4a' % (i)
        data = get_info(url)
        # print(data)
        save(data)
        time.sleep(3)
    data = load()
    download_pic(data)


if __name__ == '__main__':
    main()