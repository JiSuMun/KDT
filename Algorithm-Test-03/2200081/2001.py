import sys
sys.stdin = open("2200081/input_2001.txt", "r")
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    f = []
    # N-M+1: 파리채크기
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_ = 0
            for k in range(M):
                for l in range(M):
                    sum_ += board[i+k][j+l]
            f.append(sum_)   
    print(f'#{t} {max(f)}')