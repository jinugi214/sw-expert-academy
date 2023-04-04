# 최소비용

# 인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고,
# 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.
from collections import deque


def bfs(sx, sy):
    q = deque()

    q.append((sx, sy))

    mst[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if data[x][y] < data[nx][ny]:
                    c_val = mst[x][y] + (data[nx][ny] - data[x][y]) + 1
                else:
                    c_val = mst[x][y] + 1

                if c_val < mst[nx][ny]:
                    mst[nx][ny] = c_val
                    q.append((nx, ny))


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    mst = [[1e9] * N for _ in range(N)]
    bfs(0, 0)

    # for i in range(N):
    #     print(mst[i])

    ans = mst[N - 1][N - 1]
    print(f'#{t} {ans}')
