T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()

    check = N // 2

    ans = 1000

    for i in range(N-2):
        for j in range(i+1, N-1):
            if data[i] != data[i+1] and data[j] != data[j+1]: # 같은 크기 같은 박스에 넣어야함!
                s = i + 1
                m = j - i
                b = N - 1 - j
                if s*m*b != 0 and s <= check and m <= check and b <= check:
                    dif = max(s, m, b) - min(s, m, b)
                    ans = min(ans, dif)

    if ans == 1000:
        ans = -1

    print(f'#{t} {ans}')