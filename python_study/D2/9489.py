# title : 고대유적

T = int(input())

# 직선만 고려
# x 이동시 x만 바껴야함
# y 이동시 y만 바껴야함
dx = [1, -1] # 우하좌상
dy = [1, -1]

def dfs(x, y, cnt, xory):
    global max_v
    if cnt > max_v:
        max_v = cnt
        if max_v == limit:
            return

    visited[x][y] = 1
    # xory == 0 초기값, 1 X가 움직임, 2 Y가 움직임
    if xory == 0:
        for i in range(2):
            nx = x + dx[i]
            ny = y
            if 0 <= nx < N and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    dfs(nx, ny, cnt + 1, 1)
                    visited[nx][ny] = 0

        for i in range(2):
            nx = x
            ny = y + dy[i]
            if 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    dfs(nx, ny, cnt + 1, 2)
                    visited[nx][ny] = 0

    elif xory == 1:
        for i in range(2):
            nx = x + dx[i]
            ny = y
            if 0 <= nx < N and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    dfs(nx, ny, cnt + 1, 1)
                    visited[nx][ny] = 0

    elif xory == 2:
        for i in range(2):
            nx = x
            ny = y + dy[i]
            if 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    dfs(nx, ny, cnt + 1, 2)
                    visited[nx][ny] = 0


for t in range(1, T+1):
    # N개의 줄에 M개씩의 데이터
    N, M = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]

    limit = max(N, M)

    max_v = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                visited = [[0] * M for _ in range(N)]
                dfs(i, j, 1, 0)

    print(f'#{t} {max_v}')