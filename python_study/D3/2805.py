from collections import deque

T = int(input())


def bfs_down(x, y):
    q = deque()
    q.append([x, y])
    global revenue
    revenue += farm[x][y]
    while q:
        x, y = q.popleft()

        for i, j in zip(dx_down, dy_down):
            nx = x + i
            ny = y + j

            limit = n // 2

            if nx == limit:
                continue

            if 0 < nx < n or 0 < ny < y:
                if visited[nx][ny] == 0:
                    revenue += farm[nx][ny]
                    visited[nx][ny] = 1
                    q.append([nx, ny])

def bfs_up(x, y):
    q = deque()
    q.append([x, y])
    global revenue
    revenue += farm[x][y]
    while q:
        x, y = q.popleft()

        for i, j in zip(dx_up, dy_up):
            nx = x + i
            ny = y + j

            limit = n // 2

            if nx == limit:
                continue

            if 0 < nx < n or 0 < ny < y:
                if visited[nx][ny] == 0:
                    revenue += farm[nx][ny]
                    visited[nx][ny] = 1
                    q.append([nx, ny])


for t in range(1, T + 1):

    n = int(input())


    revenue = 0

    farm = []
    for i in range(n):
        farm.append(list(map(int, input())))

    if n == 1: # 1일 경우 입력받은 값만 출력
        revenue += farm[0][0]
        print(f'#{t} {revenue}')
        continue

    visited = [[0] * n for _ in range(n)]
    # 위에서 밑으로 bfs하면서 더하기
    dx_down = [1, 1, 1]  # 바로 밑 , 왼쪽대각아래, 오른쪽대각아래
    dy_down = [0, -1, 1]

    # 맨 위에 행의 정중앙
    x1, y1 = 0, n // 2
    bfs_down(x1, y1)

    dx_up = [-1, -1, -1] # 바로 위, 왼쪽대각위, 오른쪽대각위
    dy_up = [0, -1, 1]

    x2, y2 = n - 1, n // 2
    bfs_up(x2, y2)

    revenue += sum(farm[n // 2])

    print(f'#{t} {revenue}')

'''
# bfs가 아닌 배열을 사용해 풀어보기

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    mid = N // 2

    ans = 0

    dif = 1
    for i in range(mid-1, -1, -1):  # 행
        for j in range(dif, N - dif):  # 열
            ans += farm[i][j]
        dif += 1

    dif = 0
    for i in range(mid, N):  # 행
        for j in range(dif, N - dif):  # 열
            ans += farm[i][j]
        dif += 1

    print(f'#{t} {ans}')

'''