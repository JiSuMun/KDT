import sys
sys.stdin = open("2200081/input_10505.txt", "r")
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    average = sum(nums) / N
    cnt = 0
    for i in nums:
        if i <= average:
            cnt += 1
    print(f'#{t} {cnt}')