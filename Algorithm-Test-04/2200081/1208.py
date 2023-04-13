import sys
sys.stdin = open("2200081/input_1208.txt", "r")
for t in range(1, 11):
    n = int(input()) # 덤프 횟수
    height = list(map(int, input().split()))
    for i in range(n):
        ma, mi = max(height), min(height)
        height[height.index(ma)] -= 1
        height[height.index(mi)] += 1
    print(f'#{t} {max(height)-min(height)}')