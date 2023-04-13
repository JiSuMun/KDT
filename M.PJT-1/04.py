fruit_dict = {}

with open('./data/fruits.txt', 'r', encoding='UTF8') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()

        if fruit not in fruit_dict:
            fruit_dict[fruit] = 1

        elif fruit in fruit_dict:
            fruit_dict[fruit] += 1

with open('./04.txt', 'w', encoding='UTF8') as f:
    for fruit, count in fruit_dict.items():
        f.write(f'{fruit} {count} \n')