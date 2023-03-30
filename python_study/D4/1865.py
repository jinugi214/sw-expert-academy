T = int(input())


def dfs(idx, per):
    global ans
    if per <= ans:
        return
    if idx == N:
        if ans < per:
            ans = per
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(idx + 1, (data[idx][i] * 0.01) * per)
            used[i] = 0


for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    ans = 0
    dfs(0, 1)

    print(f'#{t} {ans*100:.6f}')
