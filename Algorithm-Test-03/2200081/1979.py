import sys
sys.stdin = open("2200081/input_1979.txt", "r")
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        a, b = 0, 0
        for j in range(N):
            if puzzle[i][j] == 1:
                a += 1
            if j == N-1 or puzzle[i][j] == 0: # 인덱스가 경계값               
                if a == K: res += 1
                a = 0
            if puzzle[j][i] == 1:
                b += 1
            if j == N-1 or puzzle[j][i] == 0:
                if b == K: res += 1
                b = 0
    print(f'#{t} {res}')