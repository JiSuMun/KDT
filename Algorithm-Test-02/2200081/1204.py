import sys
from collections import Counter
sys.stdin = open("2200081/input_1204.txt", "r")

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    print(f'#{n} {Counter(n_list).most_common()[0][0]}')