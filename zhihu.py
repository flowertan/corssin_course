#coding=utf-8

#寻找知乎大V 通过获取某一用户的关注列表，从关注列表中找出被关注数量多的用户，再从这些用户中找大V用户
#created by flower at 20170813

import requests,time
import threading
import csv

#拼接网页url,网址中含有百分号，用+进行字符串的拼接会简单一些
url1 = 'https://www.zhihu.com/api/v4/members/'
url2 = '/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&limit=20&offset='

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Host':'www.zhihu.com',
'Referer':'https://www.zhihu.com/people/tan-tan-59-96/following',
'Cookie':'_za=c0777db0-a212-4300-9a28-1b88f736946c; udid="ABBA0AjbmgmPTkI7h1ELEr0kFlGljf4yoas=|1457791006"; d_c0="AHBAWl2_vQmPTr91BEJSI3SYO0WcjaFEHF8=|1460132562"; q_c1=364c7eeb78fe4466afa2b18eac95c7f2|1500215644000|1441976745000; q_c1=364c7eeb78fe4466afa2b18eac95c7f2|1500215644000|1441976745000; _zap=a49b9e94-15d2-48d9-bd37-312fdb5b2001; capsion_ticket="2|1:0|10:1502117407|14:capsion_ticket|44:ODFiYWUzMmZmZjc0NDI5NWFkODE1OWUzZTM3OGYxYzg=|79fd49c8a2aedd4e12f87091d31cee920092130fb08493034646f0e120521ac7"; r_cap_id="YTMwZWI2NjMwNDNmNGFlZGJmMDg3OTFlNTAxNmEyYTI=|1502117410|20cd3fa851c3f882856349bc5762b075ca1092ef"; cap_id="YTA5MGY4MjllNTUxNDhhNzljOTIzNWUxY2MzZjEwNTc=|1502117410|5c1b821c2f387935fd810aa9e12f4d93fd492759"; l_cap_id="NGQ1ZGEwYmQ5YTY5NDQ2Y2E3ZjRmMGJlMTk1M2NiMzE=|1502117410|daaa4930d2cd003809955c9ef6d781183b6457f8"; z_c0=Mi4wQUJES0xNdldSZ2tBY0VCYVhiLTlDUmNBQUFCaEFsVk5UZ3l3V1FBMWpLb1F0RWNRZ2h0ZGMxOHQxLWRVb0VBTUF3|1502117710|f2c0af37abd3d3eb61c0fd89bea408232d01a1cb; aliyungf_tc=AQAAAC4nIk2ABwcAFPSh03LNzaEtVnqe; s-t=autocomplete; s-q=%E8%91%A3%E4%BC%9F%E6%98%8E; s-i=1; sid=rs8m0k58; __utma=51854390.22304212.1502629084.1502629084.1502629084.1; __utmb=51854390.0.10.1502629084; __utmc=51854390; __utmz=51854390.1502629084.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/27561422; __utmv=51854390.100--|2=registration_date=20160107=1^3=entry_date=20150911=1; _xsrf=73b28744-84f6-4667-a59c-b00e01552ebd'
}

to_crawl = ['tan-tan-59-96']
crawled = []
all_user = []
finished = threading.Event()

def crawl(url):
    #解析出json数据
    global to_crawl, crawled,finished,all_user
    time.sleep(2)
    req = requests.get(url=url, headers=headers)
    data = req.json()
    print(data)
    for user in data['data']:
        if user['follower_count'] > 600000:
            token = user['url_token']
            if token not in to_crawl and token not in crawled:
                print(user['name'])
                to_crawl.append(token)
                all_user.append([token, user['name'], user['follower_count'], user['is_following']])
                print('add token', token)
                finished.set()
    return data['paging']

def get_following(user):
    #分析某一个用户的关注列表的所有用户
    print('crawling', user)
    url = url1 + user + url2 + '0' #拼接出网址
    paging = crawl(url)

    totals = paging['totals']
    count = 20
    while count < totals and count < 1000:
        url = url1 + user + url2 + str(count)
        t = threading.Thread(target=crawl, args=(url,))
        t.start()
        count += 20

    print('to_crawl', to_crawl)
    print('crawled', crawled)

def save():
    #将获取到的大V用户信息保存到csv文件中
    with open('zhihuV.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['token', '昵称', '关注数', '是否关注'])
        for data in all_user:
            writer.writerow(data)

def main():
    while len(to_crawl):
        user = to_crawl.pop()
        crawled.append(user)

        get_following(user)

        while len(to_crawl) == 0 and threading.active_count() > 1:
            print(to_crawl, crawled)
            print('wait', threading.active_count())
            finished.clear()
            finished.wait(3)

    save()

if __name__ == '__main__':
    main()