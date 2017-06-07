import os
'''modify refer to crossin, can reserch anything'''
# path = "E:/python/test"
# key_word = 'test'
# files = []
# output = []
# def load_path():
#     for dirpath, dirnames, filenames in os.walk(path):
#         return filenames
#
#
# if __name__ == '__main__':
#     files = load_path()
#     for file in files:
#         if key_word in file:
#             output.append(file)
#             print(file)
#         else:
#             with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
#                 lines = f.readlines()
#                 for line in lines:
#                     if key_word in line:
#                         output.append(file)
#     print(files)
#     print(output)

def findfile(key, inputdir='.'):
    found_list = []
    for dirpath, dirnames, filenames in os.walk(inputdir):
        print('searching', dirpath, '...')
        for name in filenames:
            if key in name:
                found_list.append(name)
            try:
                with open(os.path.join(dirpath, name), 'r', encoding='utf-8') as f:
                    full_name = os.path.join(dirpath, name)
                    print(full_name)
                    for l in f.readlines():
                        if key in l:
                            found_list.append(full_name + ':' + l)
            except:
                print('can''t open file, no file!')
    return found_list


# def findfile(key, inputdir='.'):
#     found_list = []
#     # os.walk 获取指定目录下的所有深度的文件、子目录的列表
#
#     for path, dirnames, filenames in os.walk(inputdir):
#         print('searching', path, '...')
#         for name in filenames:
#             full_name = path + '/' + name
#             if key in name:  # 如果文件名中有关键字
#
#                 found_list.append(full_name)
#             with open(full_name, 'r', encoding='utf-8') as f:
#                 for l in f.readlines():
#                     if key in l:  # 如果当前行中有关键字
#
#                         found_list.append(full_name + ' : ' + l)
#     return found_list
keyword = input('search:')
path = input('in:')

if not path.strip():
    path = '.'

result = findfile(keyword, path)

print('\n============result================\n\n')
for r in result:
    print(r)




