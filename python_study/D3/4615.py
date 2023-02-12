T = int(input())

def othello(start_x, start_y, color):
    for i in range(8):
        x, y = start_x, start_y
        road = []
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 0:
                break
            elif color == 1 and board[nx][ny] == 1:
                for c in road:
                    cx, cy = c
                    board[cx][cy] = 1
                break
            elif color == 2 and board[nx][ny] == 2:
                for c in road:
                    cx, cy = c
                    board[cx][cy] = 2
                break
            road.append([nx, ny])
            x, y = nx, ny


# x가 좌우 # y가 위아래
dx = [0, 1, 1, 1, 0, -1, -1, -1]  # 북, 북동, 동, 동남, 남, 남서, 서, 서북,
dy = [-1, -1, 0, 1, 1, 1, 0, -1, ]

for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 1이면 흑돌 2이면 백돌
    board = [[0] * N for _ in range(N)]

    for i in range(N // 2 - 1, N // 2 + 1):
        for j in range(N // 2 - 1, N // 2 + 1):
            if (i + j) % 2 == 0:
                board[i][j] = 2
            else:
               board[i][j] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        board[x - 1][y - 1] = color

        othello(x - 1, y - 1, color)

    sb = 0
    sw = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sb += 1
            elif board[i][j] == 2:
                sw += 1

    print(f'#{t} {sb} {sw}')
