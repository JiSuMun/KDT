import sys
sys.stdin = open("2200081/input_1225.txt", "r")
for _ in range(10):
    t = int(input())
    nums = list(map(int, input().split())) # 8개
    while nums[-1] != 0:
        for i in range(1, 6):
            nums.append(nums.pop(0)-i)
            if nums[-1] <= 0: nums[-1] = 0; break
    print('#{} {} {} {} {} {} {} {} {}'.format(t, *nums))