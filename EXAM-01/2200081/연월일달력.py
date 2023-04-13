T = int(input())

for t in range(1, T+1):
    a = input()
    y = a[0:4]
    m = a[4:6]
    d = a[6:]
    d_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if 0 < int(m) < 13 and 0 < int(d) <= d_dict[int(m)]:
        print(f'#{t} {y}/{m}/{d}')
    else:
        print(f'#{t} {-1}')