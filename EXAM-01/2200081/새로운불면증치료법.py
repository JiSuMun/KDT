T = int(input())

for t in range(1, T+1):
    N = int(input())

    a = set() # 중복X
    count = 1 # 시작할때 이미 한 번 센 것
    while True:
        for n in list(str(N)): # 문자로 바꾸어 리스트에 넣으면 각 숫자의 자릿수 알 수 있음
            a.add(n)
        if len(a) == 10: # 중복 안되므로 추가했을 때 길이가 10이면 끝
            break
        N //= count
        count += 1
        N *= count # 출력을 원하는 것은 숫자를 세었을 때, 0-9 모든 숫자를 본 마지막 숫자임.
    print(f'#{t} {N}')