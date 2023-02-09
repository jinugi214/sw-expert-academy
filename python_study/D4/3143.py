# title: 가장 빠른 문자열 타이핑

T = int(input())

for t in range(1, T+1):
    a, b = input().split()

    n = len(b)

    cnt = 0
    pass_num = 0
    for i in range(len(a)):
        if pass_num > 0:
            pass_num -= 1
            continue
        if a[i] == b[0]:
            if a[i:i+n] == b:
                cnt += 1
                pass_num += n-1
            else:
                cnt += 1
                continue
        else:
            cnt += 1
    print(f'#{t} {cnt}')