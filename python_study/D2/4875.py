# title: 미로

T = int(input())

dx = [0, 1, 0, -1] # 우하좌상
dy = [1, 0, -1, 0]

def dfs(x, y):
    global ans
    if ans:
        return

    visited[x][y] = 1

    for i, j in zip(dx, dy):
        nx = x + i
        ny = y + j

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if graph[nx][ny] == '0':
                dfs(nx, ny)
                visited[nx][ny] = 0
            elif graph[nx][ny] == '3':
                ans = 1
                return

for t in range(1, T+1):
    N = int(input())

    graph = [list(input()) for _ in range(N)]

    ans = 0

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == '2':
                dfs(i, j)

    print(f'#{t} {ans}')