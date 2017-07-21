#统计奥运奖牌
#created by tch at 20170721

import random

class Medal:
    def __init__(self, countrycode = None):
        self.country = countrycode
        self.GoldMedal = 0
        self.SilverMedal = 0
        self.BronzeMedal = 0

    def add_medals(self, MedalType = None):
        if MedalType == 'Gold':
            self.GoldMedal += 1
        elif MedalType == 'Silver':
            self.SilverMedal += 1
        elif MedalType == 'Bronze':
            self.BronzeMedal += 1
        else:
            pass

    def count(self):
        return (self.BronzeMedal + self.GoldMedal + self.SilverMedal)

    def __str__(self):
        return ('{0}: gold:{1} silver:{2} bronze:{3} total:{4}'.format(self.country,self.GoldMedal, self.SilverMedal, self.BronzeMedal, self.count()))

#test class
# countryCode = 'China'
# medalType = 'Gold'
# medal1 = Medal(countryCode)
# medal1.add_medals(medalType)
# print(medal1.GoldMedal)
# print(medal1)
# countryCode = 'American'
# medal2 = Medal(countryCode)
# print(medal2.GoldMedal)
countryCode = ['China', 'America', 'Russia', 'Japan', 'Korea']
medalType = ['Gold', 'Silver', 'Bronze']

def generate_medals():
    #生成奖牌并按金牌数量和奖牌总数排名
    medals = []
    for country in countryCode:
        medal = Medal(country)
        for i in range(random.randint(2,16)):
            medal.add_medals(random.choice(medalType))
        medlaNum = medal.count()
        tup = (medal.country, medal.GoldMedal, medal.SilverMedal, medal.BronzeMedal, medlaNum)
        medals.append(tup)
    print(medals)
    return medals

def sorted_medal(medal_list, key1 = None):
    #对奖牌进行排序
    if key1 == 'gold':
        result = sorted(medal_list, key = lambda medal:medal[1], reverse = True)
        return result
    elif key1 == 'count':
        result = sorted(medal_list, key = lambda medal:medal[4], reverse = True)
        return result
    else:
        pass
    return 0

def print_medas(medals):
    #打印奖牌榜
    print('国家', '金牌', '银牌', '铜牌', '奖牌总数')
    for i in range(int(len(medals))):
        print(list(medals[i]))

def main():
    medals = generate_medals()
    result = sorted_medal(medals, 'gold')
    print_medas(result)
    result = sorted_medal(medals, 'count')
    print_medas(result)

if __name__ == '__main__':
    main()