#coding=utf-8
#抓取糗事百科热门段子
#created by flower at 20170805

import requests, time
from lxml import etree


def load_html(url):
    #获取网页数据
    req = requests.get(url)
    data = req.text
    html = etree.HTML(data)
    one_path = html.xpath('//div[@class="author clearfix"]')
    # print(one_path)
    data = ''
    for path in one_path:
        content = path.xpath('..//div[@class="content"]/span/text()')
        author = path.xpath('.//h2/text()')
        funny_count = path.xpath('..//span[@class="stats-vote"]/i/text()')
        comment_count = path.xpath('..//span[@class="stats-comments"]/a/i/text()')
        if author[0] == '匿名用户':
            age = '【未知】'
            gender = '【未知】'
        else:
            gender = path.xpath('./div/@class')[0]
            age = path.xpath('./div/text()')[0]
            if gender == 'articleGender manIcon':
                gender = '男'
            else:
                gender = '女'
        print(gender,age,funny_count,comment_count)
        print(author[0].strip())
        # print(author)
        # print(content)
        head = author[0].strip() + ' gender' + gender + ' age' + age + '\t好笑数' + funny_count[0] + '\t评论数' + comment_count[0]
        content = head + '\n' + ''.join(content) + '\n'

        data += content
    return data

def save(data):
    with open('qsbk.txt', 'a+', encoding='utf-8') as f:
        f.write(data)



def main():
    urls = 'https://www.qiushibaike.com/8hr/page/{}/'
    for page in range(1,4):
        url = urls.format(page)
        data = load_html(url)
        time.sleep(2)
        save(data)

if __name__ == '__main__':
    main()