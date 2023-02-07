data = []
line_num = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        # 算每個留言的長度，加進清單line_num
        len_line = len(line)
        line_num.append(len_line)
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
for num in line_num:
    sum = sum + num
    # 每筆留言的字數加總，除以有幾筆留言
    avg_line = sum / len(data)
print(f'留言平均長度為：{avg_line}個字')
