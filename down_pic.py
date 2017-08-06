#coding=utf8

#抓取https://pixabay.com/ 首页图片
#created by flower at 20170806

import requests
from bs4 import BeautifulSoup
import threading
header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

def download_pic(link):
    #保存图片
    try:
        r = requests.get(link,headers=header)
        filename = link.split('/')[-1]
        #print(filename)
        path = 'pics2/' + filename
        with open(path,'wb') as f:
            f.write(r.content)
    except requests.exceptions.RequestException as e:
        print(e)
        print('image download fail!')
    else:
        print('{} saved!'.format(filename))



def get_url():
    #分析并抓取网页信息
    url = 'https://pixabay.com/'
    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.text, 'lxml')
    imgs = soup.find_all('img',attrs={'srcset':True})
    pics = []
    for img in imgs:
        img_link = img.get('src')
        #print(img_link)
        pics.append(img_link)
    return pics


def main():
    pics = get_url()
    threads = []
    for i in pics:
        t = threading.Thread(target=download_pic, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

if __name__ == '__main__':
    main()