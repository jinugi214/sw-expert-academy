# title : 달팽이 숫자

T = int(input())
for t in range(1, T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    snail = [[0] * N for _ in range(N)]
    dx = [0, 1, 0, -1] # 동 남 서 북
    dy = [1, 0, -1, 0]

    idx = 0
    size = 0
    val = 1
    x, y = 0, 0
    snail[x][y] = val
    visited[x][y] = 1
    while val < N**2:
        val += 1
        x, y = x + dx[idx], y + dy[idx]
        if x >= 0 and x < N and y >= 0 and y < N and visited[x][y] == 0:
            snail[x][y] = val
            visited[x][y] = 1
        else:
            val -= 1
            x, y = x - dx[idx], y - dy[idx]
            idx += 1
            if idx == 4:
                idx = 0

    print(f'#{t}')
    for i in range(N):
        print(*snail[i])


