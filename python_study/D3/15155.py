def solve():
    for i in range(N):
        for j in range(N):
            for dx, dy in ((0, 1), (1, 0), (1, 1), (-1, 1)):
                cnt = 0
                for dif in range(5):
                    nx, ny = i+dx*dif, j+dy*dif
                    if 0 <= nx < N and 0 <= ny < N:
                        if stone[nx][ny] != 'o':
                            break
                        else:
                            cnt+=1
                else:
                    if cnt == 5:
                        return 'YES'
    return 'NO'

T = int(input())

for t in range(1, T+1):
    N = int(input())
    # 돌이 가로, 세로, 대각선 중 하나의 방향으로
    # 다섯 개 이상 연속한 부분이 있는지 없는지 판정

    stone = [list(input()) for _ in range(N)]

    print(f'#{t} {solve()}')

