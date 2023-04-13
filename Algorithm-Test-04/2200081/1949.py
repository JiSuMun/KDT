"""
최대 높이를 찾고 2차원 리스트로 탐색해서 최대 높이 m나올때마다 DFS 진행
현재위치에서 상하좌우 탐색 후 현재 위치보다 낮은 위치로 이동
else, K만큼 공사할 수 있는지 판단 후 이동
"""
import sys
sys.stdin = open("2200081/input_1949.txt", "r")
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 현재위치, 방문여부, 길이, 공사여부
def DFS(x, y, visited, step, flag):
    global ml
    # 현재위치 방문표시
    visited[x][y] = 1
    # 상하좌우탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            # 다음 위치가 현재 위치보다 낮을 때
            if M[nx][ny] < M[x][y]:
                visited[nx][ny] = 1
                DFS(nx, ny, visited, step+1, flag)
                visited[nx][ny] = 0
            # 공사 안했고, 현재 위치보다 크거나 같을 때, 공사할수있는지 판단하고 다음 위치에 최소로 높이 깎도록 공사
            # 원래 M[nx][ny]-M[x][y] < K이어야 공사 가능
            # but, 최소로 높이를 깎아야 하고, 정수 단위로만 깎을 수 있으므로 M[nx][ny]-M[x][y] <= K+1
            if flag == False and M[nx][ny] >= M[x][y] and (M[nx][ny] - M[x][y] +1) <= K: 
                visited[nx][ny] = 1
                height = M[nx][ny]
                M[nx][ny] = M[nx][ny] - (M[nx][ny] - M[x][y] +1)
                DFS(nx, ny, visited, step+1, True)
                visited[nx][ny] = 0 # 복구
                M[nx][ny] = height
    # 탐색 불가능 => 현재까지의 길이로 최댓값 비교
    ml = max(ml, step)
    visited[x][y] = 0

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]
    # 최대높이 저장
    m = 0
    # 이동한 거리 저장
    visited = [[0]*N for _ in range(N)]
    # 가장 먼 거리 저장
    ml = 0
    # 가장 높은 곳 탐색
    for i in range(N):
        for j in range(N):
            if M[i][j] > m:
                m = M[i][j]
    for i in range(N):
        for j in range(N):
            if M[i][j] == m:
                DFS(i, j, visited, 1, False)
    print(f'#{t} {ml}')