
def load_file():
    with open("words.txt", 'r', encoding='utf-8') as f:
        global block_lines
        block_lines = []
        lines = f.readlines()
        # print(lines)
        for l in lines:
            l = l.strip('\n')
            block_lines.append(l)
        # print(block_lines)
def filter_words(text, symbol = '*'):
    for w in block_lines:
        text = text.replace(w.lower(), symbol * len(w))
    return text

if __name__ == '__main__':
    load_file()
    while True:
        t = format(input('输入文字(直接回车退出): \n')).lower()
        print(t)
        if not t:
            break
        print(filter_words(t))