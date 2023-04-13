import sys
sys.stdin = open("2200081/input_14654.txt", "r")
T = int(input())
li = [3, 4, 5, 6, 9]
for t in range(1, T + 1):
    s = list(map(int, input().replace('-', '')))
    if len(s) == 16 and s[0] in li:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')