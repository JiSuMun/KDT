import sys
sys.stdin = open("2200081/input_10804.txt", "r")
T = int(input())
s_dict = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}
for t in range(1, T + 1):
    s = input()[::-1]
    st = ''
    for i in range(len(s)):
        st += s_dict[s[i]]
    print(f'#{t} {st}')
# 시간은 동일하지만 메모리가 증가
import sys
sys.stdin = open("2200081/input_10804.txt", "r")
T = int(input())
for t in range(1, T + 1):
    s = input()[::-1]
    st = ''
    for i in range(len(s)):
        if s[i] == 'b':
            st += 'd'
        elif s[i] == 'd':
            st += 'b'
        elif s[i] == 'p':
            st += 'q'
        else:
            st += 'p'

    print(f'#{t} {st}')