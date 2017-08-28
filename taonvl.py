# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2017/8/25 22:11
# @file    : taonvl.py
# @desc    : 抓取淘女郎图片
#

from selenium import webdriver
import time, os, urllib, threading
from bs4 import BeautifulSoup

url = 'https://mm.taobao.com/search_tstar_model.htm'
driver = webdriver.PhantomJS(service_args=['--load-images=no'])
all_models = []

def save_pic(img_url, filename):
    urllib.request.urlretrieve(img_url, filename)

def get_link():
    #获取淘女郎1-3页图片相关信息链接保存在列表中
    driver.set_window_size(1366, 768)
    driver.get(url)
    time.sleep(3)
    for i in range(3):
        soup = BeautifulSoup(driver.page_source, 'lxml')
        allItem = soup.find_all(class_='item')
        #print(allItem)
        all_models.extend(allItem)
        print('点击下一页')
        driver.find_element_by_link_text('下一页 >').click()
        time.sleep(3)

def get_pic_link():
    #获取主页链接
    for item in all_models:
        detail_url = item.find('a')['href']
        img = item.find('img')
        img_url = img.get('data-ks-lazyload') or img.get('src')
        name = item.find(class_='name').get_text()
        city = item.find(class_='city').get_text()
        dir_city = 'photos/' + city
        if not os.path.exists(dir_city):
            os.makedirs(dir_city)
        dir_name = dir_city + "/" + name
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if detail_url.startswith('//'):
            detail_url = 'http:' + detail_url
        if img_url.startswith('//'):
            img_url = 'http:' + img_url
        print('detail_url={}'.format(detail_url))
        print('img_url={}'.format(img_url))

        filename = dir_name + '/' + img_url.split('/')[-1]
        try:
            urllib.request.urlretrieve(img_url, filename)
        except Exception as e:
            print(e)
        get_detail(detail_url, dir_name)

def get_detail(detail_url, dir_name):
    driver.get(detail_url)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    all_img = soup.find(class_='mm-aixiu-content').find_all('img')
    #print(all_img)
    for img in all_img:
        img_url = img.get('src')
        try:
            if img_url.startswith('//'):
                img_url = 'http:' + img_url
            print('detail_img_url={}'.format(img_url))
            filename = dir_name + '/' + img_url.split('/')[-1]
            if not os.path.exists(filename):
                print('downloading', filename)
                threading.Thread(target=urllib.request.urlretrieve, args=(img_url, filename)).start()
                print(threading.active_count())
                while threading.active_count() > 3:
                    threading.Event().wait(3)
                    print(threading.active_count())
        except:
            pass


def main():
    get_link()
    get_pic_link()
    get_detail()
    driver.close()

if __name__ == '__main__':
    main()