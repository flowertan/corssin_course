import os

path = "E:/python/test"
key_word = 'test'
files = []
output = []
def load_path():
    for dirpath, dirnames, filenames in os.walk(path):
        return filenames


if __name__ == '__main__':
    files = load_path()
    for file in files:
        if key_word in file:
            output.append(file)
            print(file)
        else:
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if key_word in line:
                        output.append(file)
    print(files)
    print(output)




