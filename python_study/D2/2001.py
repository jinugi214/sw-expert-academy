def pari(x, y):
    val = 0
    for i in range(M):
        for j in range(M):
            val += data[x+i][y+j]

    return val

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            val = pari(i, j)
            if val > max_v:
                max_v = val

    print(f'#{t} {max_v}')