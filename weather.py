import json,requests

def input_city():
    city = input("你想查询哪个城市的天气?\n")
    #print(city)
    return city

def poll_weather(city):
    url = "http://wthrcdn.etouch.cn/weather_mini?city={0}".format(city)
    #print(url)
    req = requests.get(url)
    data = req.json()
   # print(data)
    return data

def output_data(data):
    result = data['data']
    #print(result)
    yesterday = result['yesterday']
    five_days = result['forecast']
    #print(yesterday)
    #print(five_days)
    for i in yesterday:
        print(yesterday[i], end=' ')
    print('\r')
    for i in five_days:
        temp = i
        for j in temp:
            print(temp[j], end=' ')
        print('\r')

if __name__ == '__main__':
    while True:
        city = input_city()
        if city == 'NO':
            break
        data = poll_weather(city)
        output_data(data)

    print('退出程序！')
