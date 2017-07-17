import re


def read_data():
    file1 = open('from.txt', encoding='utf-8')
    line = file1.read()
    file1.close()
    print(line)
    return line

def data_handle(data):
    pattern = re.compile(r'[a-zA-Z]+')
    result = pattern.findall(data)
    print(result)
    result.sort()
    print(result)
    return result

def save(data):
    file = open('to.txt', 'w', encoding='utf-8')
    temp = []
    for i in data:
        temp.append(i)
        temp.append('\n')
    print(temp)
    file.writelines(temp)
    file.close()




if __name__ == '__main__':
    data = read_data()
    result = data_handle(data)
    save(result)
