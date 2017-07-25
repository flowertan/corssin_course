#抓取煎蛋网无聊图，并保存到本地
#created by flower at 20170724

import requests, time, urllib, os
from bs4 import BeautifulSoup
import threading


img_list = []  #用来村放图片链接的列表
gLock = threading.Lock()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
img_finished = 0  # 用来判断保存图片线程结束

def get_urls():
    #煎蛋网无聊图url
    urls = ['http://jandan.net/pic/page-{0}#comments'.format(i) for i in range(int(start_page), int(end_page) + 1)]
    #print(urls)
    return urls

def get_imgs(single_url):
    #获取网页中图片链接
    header = {'User-Agent':user_agent}
    wb_data = requests.get(single_url, headers = header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('#comments > ol > li > div > div > div.text > p > img')
    gLock.acquire()
    for img in imgs:
        link = img.get('src')
        if not link.startswith('http'):
            link = 'http:' + link
        img_list.append(link)
        #print(link)
    gLock.release()
    #print(img_list)

class Producter(threading.Thread):
    def run(self):
        #解析网页获取图片链接
        print('%s is running' % threading.current_thread)
        #print(len(url_list))
        while len(url_list) > 0:
            gLock.acquire()
            url = url_list.pop()
            gLock.release()
            get_imgs(url)
            time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        #将图片保存到本地
        print('%s is running' % threading.current_thread)
        global img_finished
        while True:
            gLock.acquire()
            if len(img_list) == 0:
                gLock.release()
                if img_finished:
                    break
                continue
            else:
                img = img_list.pop()
                gLock.release()
                if len(img_list) == 0:
                    img_finished = 1
                filename = img.split('/')[-1]
                path = 'E://python/pics/'
                if not os.path.exists(path):
                    os.makedirs(path)
                full_path = os.path.join(path, filename)
                urllib.request.urlretrieve(img, filename=full_path)
                print('{} 下载完成！'.format(filename))


##comment-3497661 > div > div > div.text > p > a:nth-child(1)
##comments > ol
# #comment-3497661 > div > div > div.text > p > img:nth-child(3)
def main():
    global start_page, end_page
    global url_list# 用来存放每一页的列表
    global img_finished
    start_page = input("请输入起始页: ")
    end_page = input("请输入终止页: ")
    print("开始下载")
    url_list = get_urls()
    Producter().start()
    consumer = Consumer()
    consumer.start()
    consumer.join()
    if img_finished == 1:
        img_finished = 0
        print('图片全部下载完成')



if __name__ == '__main__':
    main()