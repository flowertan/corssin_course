# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/9/2 19:01
# @file    : shiguang.py
# @desc    :
#
from bs4 import BeautifulSoup
import requests, time, pymongo, threading, csv
from selenium import webdriver

driver = webdriver.PhantomJS()

client = pymongo.MongoClient()
db = client.shiguang
collections = db.citylists
col_movie = db.movies

cinema_list = []
result = []
city_name = ''
date = ''
movie_name = ''

#获取时光网城市列表和id
def get_city_info():
    url = 'http://m.mtime.cn/#!/citylist/'
    driver.get(url)
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    #print(soup)
    city_lists = soup.find_all('li')
    for city in city_lists:
        data = {}
        id = city.get('data-id')
        if id is not None:
            data['id'] = id
            data['name'] = city.get('data-name')
            collections.insert_one(data)
#根据城市id获取热门影片表
def get_movies(city_id):
    url = 'http://m.mtime.cn/Service/callback.mi/Showtime/LocationMovies.api?locationId={}'.format(city_id)
    req = requests.get(url)
    movie_lists = req.json()['ms']
    for movie_list in movie_lists:
        data = {}
        data['id'] = movie_list['id']
        data['name'] = movie_list['tCn']
        data['score'] = movie_list['r']
        data['type'] = movie_list['movieType']
        col_movie.update_one({'id':data['id']}, {'$set':data}, upsert=True)
        #print(data)

#根据城市id获取电影院信息
def get_cinema(city_id):
    url = 'http://m.mtime.cn/Service/callback.mi/OnlineLocationCinema/OnlineCinemasByCity.api?locationId={}'.format(city_id)
    req = requests.get(url)
    cinemas = req.json()
    for cinema in cinemas:
        data = {}
        data['id'] = cinema['cinemaId']
        data['name'] = cinema['cinameName']
        if cinema['ratingFinal'] > 8:
            cinema_list.append(data)
    print(cinema_list)

#根据电影id,电影院id,城市id日期获取票价以及场次信息
def get_detail(city_id, cinema_id, movie_id, date, cinema_name):
    url = 'http://m.mtime.cn/#!/theater/{0}/{1}/date/{2}/movie/{3}/'.format(city_id, cinema_id, date, movie_id)
    driver.get(url)
    time.sleep(3)
    #print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    start_times = soup.findAll('time')
    prices = soup.findAll(class_='msprice')
    for i in range(len(start_times)):
        data = {}
        try:
            data['start_time'] = start_times[i].text
            price = prices[i].find('strong').text
            data['price'] = price
            result.append([cinema_name, data['start_time'], data['price']])
        except Exception as e:
            print(e)
            print('没有票价信息!')

def save():
    #将获取到的信息保存到CSV文件中
    with open('shiguang_{0}_{1}_{2}.csv'.format(city_name, date, movie_name), 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['影院名称', '场次', '票价'])
        for data in result:
            writer.writerow(data)

def main():
    global city_name, date, movie_name
    city_name = input('请输入查询城市:')
    city_id = collections.find_one({'name': city_name})['id']
    get_movies(city_id)
    print('######热门影片榜######')
    for movie in col_movie.find():
        if movie['score'] <= 0:
            info = '预售'
        else:
            info = str(movie['score'])
        print(movie['name'], info, movie['type'])
    movie_name = input('请输入查询影片:')
    movie_id = col_movie.find_one({'name': movie_name})['id']
    date = input('请输入查询日期（20170902）:')
    # city_name = '上海'
    # city_id = collections.find_one({'name': city_name})['id']
    # movie_id = 236050
    # date = '20170903'
    get_cinema(city_id)
    for cinema in cinema_list:
        t = threading.Thread(target=get_detail, args=(city_id, cinema['id'], movie_id, date, cinema['name']))
        t.start()
        print(threading.active_count())
        while threading.active_count() > 3:
            threading.Event().wait(3)
            print(threading.active_count())
    print(result)
    save()
    driver.close()

if __name__ == '__main__':
    main()