import sys
sys.stdin = open("2200081/input_1983.txt", "r")
T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, T+1):
    N, K = map(int, input().split())
    score_li = []
    for i in range(N):
        score = list(map(int, input().split()))
        score_li.append(score[0]*0.35 + score[1]*0.45 + score[2]*0.2)    
    K_score = score_li[K-1] # K 점수
    score_li = sorted(score_li, reverse = 1)
    res = score_li.index(K_score) // (N // 10)
    print(f'#{t} {grades[res]}')