def bfs(sx, sy):
    q = []
    val_lst = []

    q.append((sx, sy))
    visited[sx][sy] = 1
    val_lst.append(graph[sx][sy])

    dx = [-1, 1, 0, 0]  # 서 동 북 남
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 1씩 증가하는 방뿐만 아니라 감소하는 방도 연결되는 방이기에 abs를 사용
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and abs(graph[x][y] - graph[nx][ny]) == 1:
                q.append((nx, ny))
                visited[nx][ny] = 1
                val_lst.append(graph[nx][ny])
    return min(val_lst), len(val_lst)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    rlt_val = N * N
    max_cnt = 0

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 방문하지 않은 방
                val, cnt = bfs(i, j)
                if cnt > max_cnt or cnt == max_cnt and rlt_val > val:
                    rlt_val = val
                    max_cnt = cnt

    print(f'#{t} {rlt_val} {max_cnt}')
