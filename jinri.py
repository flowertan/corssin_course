#coding=utf-8

#抓取今日头条体育版块信息
#created by flower at 20170814

import requests, time, csv

url1 = 'http://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time='
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Host':'www.toutiao.com',
    'Referer':'http://www.toutiao.com/ch/news_sports/',
    'Cookie':'uuid="w:bcacd4cc1c4a41baaf6b1ed7c5ff5e65"; UM_distinctid=15b43b8d085225-0f2091cded6b7b-52633074-a41c3-15b43b8d0862a8; _ga=GA1.2.1973228534.1491489838; csrftoken=28d9f2589ceb7fc607fb0676a0c49189; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6454111257205065229; CNZZDATA1259612802=1202933936-1491487878-null%7C1502711969; __tasessionId=25ps8nnl51502714902320'
}
all_info = []

def crawl(url):
    #获取json数据
    time.sleep(2)
    req = requests.get(url=url, headers=headers)
    data = req.json()
    print(data)
    for info in data['data']:
        try:
            all_info.append([info['title'], info['abstract'], info['comments_count']])
        except Exception as e:
            print(e)
            continue

    return data['next']

def save():
    with open('jinrisport.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题', '概述', '评论数'])
        for info in all_info:
            writer.writerow(info)

def get_info():
    url = url1 + '1502716011'
    for i in range(5):
        next = crawl(url)
        url = url1 + str(next['max_behot_time'])



def main():
    get_info()
    save()

if __name__ == '__main__':
    main()