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

cookie = '_zap=748357d0-9b01-4e10-a9bb-9febb39e9d06; d_c0="AIDn6XqpRQ6PTgSvPZvdPbNjSymLBjAwxGQ=|1537973108"; _xsrf=aA6YTNLTvYsVirD4QESE7LGPNVu3uxLJ; q_c1=5ee6f8afff69479ca5ffd4fe4c50add1|1557965419000|1542634947000; capsion_ticket="2|1:0|10:1567784051|14:capsion_ticket|44:ZmJhNzE5OTZhODQxNDNmM2FhNjM2NTM3NGRkMzg5Zjk=|70617939de04f7a30edd825dac4137d1785449f9c15a5ba2b9be0186ddf2ee03"; l_n_c=1; r_cap_id="NGU1Nzg4MGU5MjJmNGE5OTliMzY1MThiYzBhNmRjN2I=|1567784055|87017b267a12aff00bb6aa1cf4b422bd5a7fab4d"; cap_id="NzEyMDY3ZWQ4ZTU1NDk2NmIyNDA3ZTYxNWQxNDY3OWY=|1567784055|4f9f24b8d29166b6cca0e4df35c99fa16d73076f"; l_cap_id="YmUwNzJjYmQ3ZWVhNDIyMWE1MmFlZjEwMjc4YmQ5ZmY=|1567784056|8fc25139d73bb6ebf72297325b10e8cdfce90789"; n_c=1; z_c0=Mi4xaXloMEFnQUFBQUFBZ09mcGVxbEZEaGNBQUFCaEFsVk5nc3BmWGdEZXJBOHdLckZzeWRmdkxrX2dJNHpmSGUwNk1B|1567784066|e7b4e0b4d6742dd1cfff19ced6c3997e42599ff4; tst=r; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7'

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

