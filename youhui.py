# import random
# import string
#
# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
# for i in range(0,200):
#     a = list(string.ascii_letters) + list(string.digits)
#     random.shuffle(a)
#     final = ''.join(a[:8])
#     print("{}".format(final))
#coding=utf8
#modify by flower at 20170728
#采用另外一种思路编写生成优惠券码
import random

result = []#存放200个优惠券

def one_data():
    one = []  # 用来存放一个优惠券码
    for i in range(8):
        temp = [chr(random.randint(65, 90)), chr(random.randint(97, 122))]
        one.append(random.choice(temp))
    return (''.join(one))

for i in range(200):
    str_one = one_data()
    if str_one not in result:
        result.append(str_one)
    else:
        str_one = one_data()
        result.append(str_one)
print(result)

