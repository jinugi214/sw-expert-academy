# 탈주범은 시간당 1의 거리를 움직일 수 있다.
# 탈주범이 있을 수 있는 위치의 개수를 계산

T = int(input())

for t in range(1, T + 1):
    # 지하 터널 지도의 세로 크기 N, 가로 크기 M,
    # 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C,
    # 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())

    tunnel = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    # 이동과 제자리에 있는 경우 포함
    type = {1: [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)],
            2: [(-1, 0), (1, 0), (0, 0)],
            3: [(0, -1), (0, 1), (0, 0)],
            4: [(-1, 0), (0, 1), (0, 0)],
            5: [(1, 0), (0, 1), (0, 0)],
            6: [(1, 0), (0, -1), (0, 0)],
            7: [(-1, 0), (0, -1), (0, 0)]}

    # 각 이동할 때마다 연결된 부위
    connect = {(-1, 0): [1, 2, 5, 6], (1, 0): [1, 2, 4, 7], (0, -1): [1, 3, 4, 5], (0, 1): [1, 3, 6, 7],
               (0, 0): [1, 2, 3, 4, 5, 6, 7]}

    visited[R][C] = 1  # 맨홀 뚜껑

    q = [(R, C)]
    for _ in range(L):
        for _ in range(len(q)):
            x, y = q.pop(0)
            for dx, dy in type[tunnel[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and tunnel[nx][ny] in connect[(dx, dy)]:
                    # 가로 세로 길이 다르고 연결되는 부위끼리만 이동 가능
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1 # 방문할 때마다 횟수 갱신

    cnt = 0

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{t} {cnt}')
