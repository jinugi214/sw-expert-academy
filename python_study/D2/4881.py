def dfs(x, y, val, cnt):
    global min_v
    if min_v < val:
        return

    visited[x] = 1

    val += data[x][y]

    if cnt == N and val < min_v:
        min_v = val
        return

    for x in range(N):
        if not visited[x] and y < N-1:
            dfs(x, y+1, val, cnt+1)
            visited[x] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    min_v = 1e9
    for i in range(N):
        visited = [0] * N
        dfs(i, 0, 0, 1)

    print(f'#{t} {min_v}')