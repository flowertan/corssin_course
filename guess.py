import random

total = 0 #总轮数
times = 0 #一轮猜的次数
success = 0

you_choice = input("GAME START YES OR NO:")
while True:
    if you_choice == 'YES':
        total += 1
        goal = random.randint(1, 100)
        while True:
            you_guess = input("please input a num:")
            times += 1
            # print(times)
            if times > 5:
                print("you have guess more than 5 times you guess fail!!the goal is {}".format(goal))
                times = 0
                you_choice = 'end'
                break
            elif int(you_guess) < goal:
                print(you_guess, 'too small!!')
            elif int(you_guess) > goal:
                print(you_guess, "too big!!")
            else:
                success += times
                print(you_guess, "you got it!!")
                times = 0
                you_choice = input("GAME START YES OR NO:")
                break
    elif you_choice == 'end':
        print("GAME OVER")
        break
    else:
        print('you don\'t want to go')
        break

try:
    avg = success / total
except:
    avg = 0
    pass
print("你总共玩了{}轮,平均{}次猜中".format(total, int(avg)))
