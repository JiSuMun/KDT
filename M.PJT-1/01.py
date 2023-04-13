str_list = [
    'Hello, Python!',
    '1일차 파이썬 공부 중',
    '2일차 파이썬 공부 중',
    '3일차 파이썬 공부 중',
    '4일차 파이썬 공부 중',
    '5일차 파이썬 공부 중'
]

with open('./01.txt', 'w', encoding='UTF8') as f:
    for str in str_list:
        f.write(str + '\n')
