T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    sum = 0
    for i in nums:
        if i % 2 == 1:
            sum += i
    print(f'#{t} {sum}')