#coding=utf-8

#通过豆瓣API获取数据保存到MongoDB中
#created bu flower at 20170817

import requests, time
import pymongo

client = pymongo.MongoClient()
db = client.douban
collection = db.movies
col_casts = db.casts
#获取豆瓣排名top250的电影
# for start in range(0, 250, 20):
#     print('fetching', start)
#     url = 'https://api.douban.com//v2/movie/top250?start=' + str(start)
#     req = requests.get(url)
#     data = req.json()
#     print('inserting', start)
#     collection.insert_many(data['subjects'])
#     print('finish', start)
def get_casts(id):
    if not id:
        return
    print('feching', id)
    try:
        url = 'https://api.douban.com/v2/movie/celebrity/' + str(id)
        req = requests.get(url)
        data = req.json()
        print('updating', id)
        col_casts.update_one({'id': data['id']}, {'$set': data}, upsert=True)
        print('Done')
    except Exception as e:
        print(e, id)

for movie in collection.find():
    casts = movie['casts']
    for cast in casts:
        print(cast['name'], cast['id'])
        get_casts(cast['id'])
        time.sleep(1.5)
