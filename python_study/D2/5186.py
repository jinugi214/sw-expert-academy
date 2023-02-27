T = int(input())

for t in range(1, T+1):
    N = float(input())

    num = 1

    ans = ''

    for i in range(12):
        num *= 0.5
        if N - num >= 0:
            ans += '1'
            N -= num
        elif not N:
            break
        else:
            ans += '0'

    if N > 0:
        ans = 'overflow'

    print(f'#{t} {ans}')