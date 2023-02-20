# 讀取檔案
def read_file(filename):
    lines = []
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
            lines.append(line)
            if count % 10000 == 0:
                print(f'讀取了{count}筆資料')
    return lines

def split(lines):
    wc = {} # word_count
    print('開始建立單詞出現次數字典......')
    for line in lines:
        words = line.split() # 預設就是空白鍵，且遇到連續空白會直接忽視
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1
    return wc


def find_word(wc):
    while True:
        word = input('請輸入欲查尋的單詞: ')
        if word == 'q':
            ask = input('是否要結束查詢(y/n): ')
            if ask == 'y' or 'Y':
                break
            else:
                continue
        if word in wc:
            print(wc[word])
        else:
            print('查無此單詞')


def main():
    filename = 'reviews.txt'
    lines = read_file(filename)
    wc = split(lines)
    find_word(wc)

if __name__ == '__main__':
    main()