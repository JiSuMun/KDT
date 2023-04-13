# 두 번째 for문에서 square 리스트의 첫 인덱스를 count
# 2로 나눈 나머지가 1이면 그 숫자를 출력
# 336ms
import sys
sys.stdin = open("2200081/input_3456.txt", "r")
T = int(input())
for t in range(1, T + 1):
    square = list(map(int, input().split()))
    for i in range(3):
        if square.count(square[i]) % 2 == 1:
            print(f'#{t} {square[i]}')
            break
# 291ms
import sys
sys.stdin = open("2200081/input_3456.txt", "r")
T = int(input())
for t in range(1, T+1):
    a, b, c = input().split()
    if a == b:
        r = c
    else:
        if a == c:
            r = b
        else:
            r = a
    print(f'#{t} {r}')