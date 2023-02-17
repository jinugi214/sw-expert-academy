# title : 우주선착륙2

T = int(input())

dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 북, 북동, 동, 동남, 남, 남서, 서, 서북
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def check(x, y):

    cnt = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if mars[x][y] > mars[nx][ny]:
                cnt += 1

    if cnt >= 4:
        global ans
        ans += 1


for t in range(1, T+1):
    N, M = map(int, input().split())
    mars = [list(map(int, input().split())) for _ in range(N)]

    # 현재위치의 주변 8개의 방향 중 4개이상이 현재위치보다 낮은 숫자이면 후보지 포함

    # 모서리는 주변이 4지역이상이 아니기에 제외

    ans = 0

    for i in range(N):
        for j in range(M):
            if [i, j] in [[0, 0], [0, M-1], [N-1, 0], [N-1, M-1]]:
                continue
            else:
                check(i, j)

    print(f'#{t} {ans}')