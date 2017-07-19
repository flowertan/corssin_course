import re

#统计文本里面单词个数
#created by flower_tan at 20170719

def data_handle(data):
    #处理数据
    pattern = re.compile(r'\S+') #\S 匹配除了空格之外的所有字符
    result = pattern.findall(data)
    print(result)
    print('There are {0} words in compositon.txt'.format(len(result)))

def loadfile():
    #open txt
    file = open('composion.txt', 'r', encoding='utf-8')
    words_list = file.read()
    print(words_list)
    file.close()
    return words_list

def main():
    words = loadfile()
    data_handle(words)


if __name__ == '__main__':
    main()