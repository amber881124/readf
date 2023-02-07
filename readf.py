data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        # 將每筆留言加入清單data
        data.append(line.strip())
        count += 1
        # 每100000筆印一次長度(得知讀取進度)
        if count % 100000 == 0:
            print(len(data))
print('結束囉!')
print(f'共有{len(data)}筆留言')

# 印出前三筆留言
for i in range(3): 
    print(f'第{i+1}筆留言為: ')
    print(data[i])
    print('-----------')

# 計算留言平均長度
sum = 0
for review in data:
    review_len = len(review)
    sum = sum + review_len
    # 每筆留言的字數加總，除以有幾筆留言
    avg_line = sum / len(data)
print(f'留言平均長度為：{avg_line}個字')
