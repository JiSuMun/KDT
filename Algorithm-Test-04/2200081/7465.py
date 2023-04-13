import sys
sys.stdin = open("2200081/input_7465.txt", "r")
from collections import deque

def BFS(start):
    d = deque([start])
    visited[start] = 1 # 시작점 방문처리
    while d:
        c = d.popleft()
        for i in p[c]:
            if visited[i] == 0:
                d.append(i) # 새로운 방문 추가
                visited[i] = 1 # 방문처리
T = int(input())
for t in range(1, T+1):
    N , M = map(int, input().split()) # 사람 수, 서로 알고있는 사람의 관계수
    p = [[] for _ in range(N+1)] # 인접리스트
    visited = [0]*(N+1)
    cnt = 0 # 무리개수
    for _ in range(M):
        a, b = map(int, input().split())
        p[a].append(b)
        p[b].append(a)
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1 # 방문하지 않았으므로 무리개수+1 하면서 BFS
            BFS(i)
    print(f'#{t} {cnt}')