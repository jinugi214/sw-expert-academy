T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    max_v = 0
    min_v = 1e9
    for i in range(N-M+1):
        val = 0
        for j in range(i, i+M):
            val += data[j]

        if val > max_v:
            max_v = val
        if val < min_v:
            min_v = val

    ans = max_v - min_v

    print(f'#{t} {ans}')