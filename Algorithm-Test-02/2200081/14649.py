import sys
sys.stdin = open("2200081/input_14649.txt", "r")
T = int(input())
for t in range(1, T + 1):
    result = 0
    N = 0
    nums = list(map(int, input().split()))
    for i in range(15):
        if i % 2 == 0: # 홀수자리는 인덱스로 봤을 때 짝수
            result += nums[i] * 2
        elif i % 2 == 1:
            result += nums[i]
    if result % 10 == 0:
        N = 0
    else:
        N = 10 - ((result) % 10)
    print(f'#{t} {N}')