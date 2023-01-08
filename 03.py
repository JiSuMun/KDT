fruit_list = []
count = 0

with open('./data/fruits.txt', 'r', encoding='UTF8') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()
        if fruit[-5:] == 'berry':
            if fruit not in fruit_list:
                fruit_list.append(fruit)
                count += 1

with open('./03.txt', 'w', encoding='UTF8') as f:
    f.write(str(count) + '\n')
    for fruit in fruit_list:
        f.write(fruit + '\n')