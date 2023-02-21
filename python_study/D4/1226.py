def bfs(start_x, start_y):
    q = [(start_x, start_y)]

    visited = [[0] * N for _ in range(N)]

    while q:
        x, y = q.pop(0)
        dx = [1, -1, 0, 0]  # 동 서 남 북
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
            elif 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 3:
                return 1
    return 0


N = 16

for t in range(1, 11):
    _ = input()
    graph = [list(map(int, input())) for _ in range(N)]

    ans = bfs(1, 1)

    print(f'#{t} {ans}')
