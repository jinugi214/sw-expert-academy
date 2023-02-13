def recur(n, cnt):
    if cnt == M:
        return n

    return recur(n*N, cnt+1)


for t in range(1, 11):
    _ = int(input())
    N, M = map(int, input().split())

    ans = recur(N, 1)

    print(f'#{t} {ans}')