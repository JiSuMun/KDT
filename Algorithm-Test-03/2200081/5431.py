import sys
sys.stdin = open("2200081/input_5431.txt", "r")
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split()) # 수강생 수, 제출자 수
    k_li = list(map(int, input().split())) # 제출자들의 번호
    n_li = []
    for i in range(1, N+1):
        if i not in k_li:
            n_li.append(i)
    print(f'#{t}', *n_li)