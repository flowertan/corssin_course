# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/9/10 22:06
# @file    : zufang.py
# @desc    : 抓取上海链家网租房信息
#

import requests, csv, time
from bs4 import BeautifulSoup as bs

# 通过谷歌浏览器查看cookie
cookie = 'lianjia_uuid=5bbacdf7-bf51-4351-8dab-19dca0f3f8a8; XXXXXXXXX3p1ZmFuZy9wZzEiLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

headers = {'User-Agent':user_agent, 'cookie':cookie}


def main():
    with open('zufang.csv', 'a+', newline='', encoding='utf-8-sig') as f:
        for i in range(1, 20):
            url = 'https://sh.lianjia.com/zufang/pg%d' % (i)
            req = requests.get(url, headers=headers)
            # print(req.text)
            # 解析网页信息
            soup = bs(req.text, 'lxml')
            # 找到租房信息在网页中的位置
            contents = soup.findAll(class_='content__list--item--main')
            # print(contents)
            for content in contents:
                data = []
                # 租房的详细信息链接
                link = content.find('a').get('href')
                # print(link)

                # 租房信息的title
                title = content.find('a').text
                # print(title.split())
                # print(" ".join(title.split()))

                data.append(" ".join(title.split()))
                data.append(link)

                p = content.find('p', class_='content__list--item--des')
                info = p.text.split()
                # print(("".join(info)).split('/'))

                for index in (("".join(info)).split('/')):
                    data.append(index)
                # print(data)

                bottom = content.find('p', class_='content__list--item--bottom')
                extention = []
                for i in bottom.findAll('i'):
                    extention.append(i.text)
                # print(",".join(extention))

                data.append(",".join(extention))
                # print(bottom.findAll('i'))
                price = content.find('em')
                # print(price.text)
                data.append(price.text)
                print(data)
                csv_file = csv.writer(f)
                csv_file.writerow(data)
            time.sleep(3)


if __name__ == '__main__':
    main()
'''
//*[@id="content"]/div[1]/div[1]/div[1]/div/p[1]/a
'''
'''
#content > div.content__article > div.content__list > div:nth-child(1) > div > p.content__list--item--title.twoline > a
#content > div.content__article > div.content__list
<p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/SH2341183411986898944.html">
          整租·梅陇十一村 1室1厅 南        </a>
      </p>
      #content > div.content__article > div.content__list > div:nth-child(1) > div
'''