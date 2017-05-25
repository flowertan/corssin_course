import random
import string

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
for i in range(0,200):
    a = list(string.ascii_letters) + list(string.digits)
    random.shuffle(a)
    final = ''.join(a[:8])
    print("{}".format(final))
