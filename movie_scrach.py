# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/8/28 21:22
# @file    : movie_scrach.py
# @desc    : 糯米网电影票价信息
#

import requests, pymongo, time, csv, threading
from bs4 import BeautifulSoup

#城市列表接口
# url = 'https://dianying.nuomi.com/common/city/citylist?hasLetter=false&isjson=false&channel=&client='

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
#     'Referer':'https://dianying.nuomi.com/index',
#     'Host':'dianying.nuomi.com',
#     'Cookie':'access_log=292488c381106d5a14164657c5e4985f; channel_content=f4dcb0820002efc70000000359a4110c; Hm_lvt_a028c07bf31ffce4b2d21dd85b0b8907=1503924502; Hm_lpvt_a028c07bf31ffce4b2d21dd85b0b8907=1503924502; areaCode=2400010000; BDUSS=MxRTBHZGxHUnBPV052aUJoYlhqRkxoRVpwVzY2OXo5MHRaakxtV3FuTXpoVTVaSVFBQUFBJCQAAAAAAAAAAAEAAABh97YbdGFuY2h1bmh1YV85MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADP4Jlkz-CZZdV; STOKEN=62a9f5609bec873c77a2fbdfc88ef78e3256c9690fff25d2afceb47105520c6a; domainUrl=nc; flag=001; gpsGot=0; channel=www.baidu.com_other%7C%7C; channel_webapp=webapp; BAIDUID=7F3BD65664E9CFB74995D31675598171:FG=1; MOVIE_SELECT=%7B%22cityId%22%3A%22289%22%2C%22cityName%22%3A%22%E4%B8%8A%E6%B5%B7%22%7D'
# }

client = pymongo.MongoClient()
db = client.nuomi
col_city = db.citylist
col_hotmovie = db.hotmovielist

#将城市列表保存到数据库中供查询城市的时候使用
# req = requests.get(url=url, headers=headers)
# data = req.json()
# print(data['data'])
# hot_lists = data['data']['hot']
# print(hot_lists)
# for hot_list in hot_lists:
#     col_city.update_one({'id':hot_list['id']}, {'$set':hot_list}, upsert=True)
# all_lists = data['data']['all']
# print(all_lists)
# for all_list in all_lists:
#     col_city.update_one({'id':all_list['id']}, {'$set':all_list}, upsert=True)

#0829计划完成热映影片获取 对提取网页信息应用不熟
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'
}
movielist = [] #存放热门影片信息
cinemalist = [] #影院
result = []
city_name = ''
date = ''
movie_name = ''
def get_hot_movie(city_id):
    url = 'https://mdianying.baidu.com/movie/movie?sfrom=newnuomi&sub_channel=nuomi_wap_rukou1&c=289&cc=289&lat=&lng=&device=2.0000000298023224_380_&subTabIdx=0&query%5BmovieCinemaTabIdx%5D=0&query%5BsubTabIdx%5D=0&query%5BpageId%5D=portal%2FmovieCinema&query%5Btitle%5D=%E7%94%B5%E5%BD%B1&query%5Bvoucher%5D=false&movieCinemaTabIdx=0&pageId=portal%2FmovieCinema&title=%E7%94%B5%E5%BD%B1&voucher=false'
    req = requests.get(url=url, headers=headers)
    data = req.json()
    #print(data['data']['html'])
    wb_data = data['data']['html']
    soup = BeautifulSoup(wb_data, 'lxml')
    # print(soup)
    movieinfo_lists = soup.find_all(class_='movie-detail-link')
    # print(movieinfo_lists)
    for info in movieinfo_lists:
        movie = {}
        data = info.get('data-log')
        name = info.find(class_='movie-name-text')
        data = eval(data)
        movie['id'] = data['movieId']
        movie['name'] = name.text
        try:
            movie['score'] = info.find(class_='fen').text
        except:
            movie['score'] = info.find(class_='movie-focus').text

        movie['type'] = info.find(class_='movie-time movie-type').text
        # print(movie)
        col_hotmovie.update_one({'id':movie['id']}, {'$set':movie}, upsert=True)
        movielist.append(movie)
    #print(movielist)

#0830 计划完成热门影院信息提取, 实际0902完成
def get_cinema_info(city_id):
    for i in range(3):
        #抓取3页影院信息
        url = 'https://mdianying.baidu.com/movie/cinema?sfrom=wise_shoubai&sub_channel=&c={0}&cc={1}&lat=&lng=&device=2.0000000298023224_380_&pn={2}&isAppend=1&areaId=&aoiId=&metroLineId=&metroStationId=&brandId=&featureId=&filterId='.format(city_id, city_id,i)
        req = requests.get(url=url, headers=headers)
        data = req.json()
        #print(data['data'])
        wb_data = data['data']['html']
        soup = BeautifulSoup(wb_data, 'lxml')
        #print(soup)
        cinema_lists = soup.find_all(class_='portal-cinema-list-item-link')
        for info in cinema_lists:
            data = {}
            detail_info_href = info.get('href')
            detail_url = detail_info_href.split('#')[0]
            data['link'] = detail_url
            #print(detail_url)
            name = info.find(class_='portal-cinema-name').text
            # print(name)
            data['name'] = name
            cinemalist.append(data)
        time.sleep(1)
    print(cinemalist)

def get_detail(link, movieId, date, city_id, cinema_name):
    url = 'https://mdianying.baidu.com{0}&sfrom=wise_shoubai&from=webapp&active_movie_id={1}&movieId={2}&date={3}&sub_channel=&source=&c={4}&cc={5}&kehuduan=#showing'.format(link, movieId, movieId, date, city_id, city_id)
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    #print(soup)
    try:
        movie_info = soup.find(class_='schedule active date-{0} movie-{1}'.format(date, movieId))
        #print(movie_info)
        start_time = movie_info.find_all(class_='start')
        prices = movie_info.find_all(class_='price')
        for i in range(len(start_time)):
            data = {}
            data['name'] = cinema_name
            data['time'] = start_time[i].text
            price = prices[i].text
            data['price'] = price[5:7]
            result.append([data['name'], data['time'], data['price']])
    except Exception as e:
        print(e)
        print('get info failed!!!')
    time.sleep(3)


def save():
    with open('nuomi_{0}_{1}_{2}.csv'.format(city_name, date, movie_name), 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['影院名称', '场次', '票价'])
        for data in result:
            writer.writerow(data)

def main():
    global city_name, date, movie_name
    print('######热门影片榜######')
    for info in col_hotmovie.find():
        print(info['name'], info['score'], info['type'])

    city_name = input('请输入查询城市:')
    city_id = col_city.find_one({'name': city_name})['id']

    movie_name = input('请输入查询影片:')
    movie_id = col_hotmovie.find_one({'name': movie_name})['id']

    date = input('请输入查询日期（年月日以-间隔）:')
    print(city_id, movie_id)

    timeArray = time.strptime(date, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))
    date = str(timeStamp) + '000'

    get_cinema_info(city_id)
    for info in cinemalist:
        t = threading.Thread(target=get_detail, args=(info['link'], movie_id, date, city_id, info['name']))
        t.start()
    t.join()
    print(result)
    save()





if __name__ == '__main__':
    main()