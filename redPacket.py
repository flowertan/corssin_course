#简单的微信随机红包小程序
#生成people个0到1之间的随机数，将随机数相加，按照比例算出每一个红包金额
#created by flower at 20170727

import random

def redPacket(people, money):
    s = 0
    result = []
    money *= 100
    for i in range(people):
        x = random.uniform(0,1)
        result.append(x)
        s += x
    for i in range(people):
        result[i] = round(result[i] / s *money / 100.0, 2)
    return result

def main():
    people = int(input('请输入人数: '))
    money = int(input('请输入金额: '))
    result = redPacket(people, money)
    print(result)


if __name__ == '__main__':
    main()


