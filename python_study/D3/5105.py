def bfs(start_x, start_y):

    used = [[0] * N for _ in range(N)]

    q = [(start_x, start_y, 0)]

    while q:
        x, y, cnt = q.pop(0)
        used[x][y] = 1

        dx = [0, 0, 1, -1] # 동, 서, 남, 북
        dy = [1, -1, 0, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not used[nx][ny] and graph[nx][ny] == 0:
                q.append((nx, ny, cnt+1))
            elif 0 <= nx < N and 0 <= ny < N and not used[nx][ny] and graph[nx][ny] == 3:
                return cnt
    return 0

T = int(input())

for t in range(1, T+1):
    N = int(input())

    graph = [list(map(int, input())) for _ in range(N)]

    brk = False

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                ans = bfs(i, j)
                brk = True
                break
        if brk:
            break

    print(f'#{t} {ans}')