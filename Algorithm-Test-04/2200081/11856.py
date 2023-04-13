import sys
sys.stdin = open("2200081/input_11856.txt", "r")
from collections import Counter
T = int(input())
res = 0
for t in range(1, T+1):
    S = input().rstrip()
    s = Counter(S).most_common()
    for i in s:
        if len(i) == 2 and i[1] == 2: res = 'Yes'
        else: res = 'No'
    print(f'#{t} {res}')