import sys
sys.stdin = open("2200081/input_1218.txt", "r")
a = {'(':')', '[':']', '{':'}', '<':'>'}
for t in range(1, 11):
    res = 1
    N = int(input())
    s = input()
    stack = []
    for i in s: # 왼쪽을 스택에 저장하면서 오른쪽부터 비교
        if i in a.keys(): stack.append(i)
        else:
            if a[stack[-1]] == i: stack.pop()
            else: res = 0; break
    print(f'#{t} {res}')