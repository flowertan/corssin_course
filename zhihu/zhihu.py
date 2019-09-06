# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/9/6 23:30
# @file    : zhihu.py
# @desc    : 爬取知乎页面
#
'''
http://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=1c21304776b90c900da9cfa353d7bab0&desktop=true&page_number=2&limit=6&action=down&after_id=5
http://www.zhihu.com/api/v3/feed/topstory/recommend?limit=10&desktop=true
'''
import requests,csv,time
# 非真实cookie, 需要使用自己登录后查看cookie
cookie = 'xxxxxxxEFsVk5nc3BmWGdEZXJBOHdLckZzeWRmdkxrX2dJNHpmSGUwNk1B|1567784066|e7b4e0b4d6742dd1cfff19ced6c3997e42599ff4; tst=rxxxxxx'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
referer = 'https://www.zhihu.com/'

headers = {'User-Agent':user_agent, 'cookie':cookie, 'referer':referer}

# 文件头
head = ['id', 'title', 'author_name', 'followers', 'type']


def main():
    with open('data.csv', 'a+', newline='', encoding='utf-8-sig') as f:
        for i in range(1,101):
            info = []
            url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=1c21304776b90c900da9cfa353d7bab0&desktop=true&page_number=%d&limit=6&action=down&after_id=%d' % (i, 6*(i-1)+5)

            req = requests.get(url, headers=headers)
            # print(req.json())
            contents = req.json()
            # print(contents.get('data'))
            for content in contents.get('data'):
                temp = {}
                # print(content)
                try:
                    temp['id'] = content.get('id')
                    target = content.get('target')
                    question = target.get('question')
                    # print(question)
                    temp['title'] = question.get('title')
                    temp['author_name'] = target.get('author').get('name')
                    print(target.get('author'))
                    temp['followers'] = target.get('author').get('followers_count')
                    temp['type'] = content.get('action_text')
                    print(temp)
                except Exception as e:
                    print(e)
                    continue
                finally:
                    info.append(temp)
            time.sleep(3)
            csvfile = csv.DictWriter(f, head)
            csvfile.writerows(info)


if __name__ == '__main__':
    main()

