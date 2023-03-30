T = int(input())


def dfs(sx, sy, val, cnt):
    used[sy] = 1
    global ans
    if val > ans:
        return

    if cnt == N:
        if val < ans:
            ans = val
        return

    for dy in range(N):
        nx, ny = sx + 1, dy
        if 0 <= nx < N and 0 <= ny < N:
            if not used[ny]:
                dfs(nx, ny, val + data[nx][ny], cnt + 1)
                used[ny] = 0


for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e9
    for i in range(N):
        used = [0] * N
        dfs(0, i, data[0][i], 1)

    print(f'#{t} {ans}')
