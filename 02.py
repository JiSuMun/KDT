f = open('data/fruits.txt', 'r', encoding='UTF8')

cnt = 0
while True:
    if f.readline() == '':
        break
    cnt += 1
f.close()

with open('./02.txt', 'w') as f:
    f.write(str(cnt))