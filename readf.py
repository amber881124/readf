data = []

with open('test.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
print(data)