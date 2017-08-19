# coding=utf-8
#
# @Version : 1.0
# @Time    : 2017/08/19 15:38
# @Author  : flower
# @File    : music.py
#
# 网易云API根据关键词提取歌词

import requests, time, threading
import pymongo

#网易API请求头
headers = {
    'Cookie': 'appver=1.5.0.75771',
    'Referer': 'http://music.163.com/'
}

#建立MongDB客户端
client = pymongo.MongoClient()
db = client.wangyi
collections = db.musiclist
col_lyc = db.musiclyc


key_word = '热干面'
info = {
    's': key_word,
    'offset': 1,
    'limit': 10,
    'type': 1000
}

def get_playlists_id():
    url = 'http://music.163.com/api/search/pc'
    req = requests.post(url= url, data=info, headers=headers)
    content = req.json()
    print(content['result'])
    # collections.delete_one(content['result'])
    playlists = content['result']['playlists']
    for playlist in playlists:
        collections.update_one({'id': playlist['id']}, {'$set': playlist}, upsert=True)

def get_lyc(id):
    #根据歌曲id获取歌词保存到数据库中
    url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'.format(id)
    req = requests.get(url=url, headers=headers)
    data = req.json()
    try:
        print(data['lrc'])
        col_lyc.insert(data['lrc'])
        time.sleep(2)
    except Exception as e:
        print(e, id)

def get_music_id():
    #根据歌单id获取歌曲id
    for playlist in collections.find():
        #print(playlist['id'])
        url = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'.format(playlist['id'])
        req = requests.get(url=url, headers=headers)
        data = req.json()
        #print(data['result']['tracks'])
        tracks = data['result']['tracks']
        for track in tracks:
            #print(track['id'])
            #get_lyc(track['id'])
            t = threading.Thread(target=get_lyc, args=(track['id'],))
            t.start()


def main():
    get_playlists_id()
    get_music_id()

if __name__ == '__main__':
    main()