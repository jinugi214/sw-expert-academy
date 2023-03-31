# 디저트 카페

''' 조건
1. 대각선 방향으로 움직이며 사각형 모양을 그리며 사격형 모양을 만들어야한다.
2. 이동하면서 같은 숫자가 있으면 안됨
3. 한 곳에서만 디저트를 먹으면 안됨
4. 왔던 길을 다시 돌아가는 것도 안됨
'''

# 남동, 남서, 북서, 북동 4가지 방향
move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(x, y, path, m_idx):
    global cnt, i, j

    # 원래 위치로 돌아오고 사각형을 만들기 위해 북동방향 이동과 지금껏 4번이상 이동했는 경우
    if x == i and y == j and m_idx == 3 and len(path) > 3:
        cnt = max(cnt, len(path))
        return

    # 범위 확인 및 현재 경로에 포함되지 않은 곳이면
    if 0 <= x < N and 0 <= y < N and data[x][y] not in path:
        new_path = path + [data[x][y]] # 경로에 현재 값 추가

        # 직진
        nx, ny = x + move[m_idx][0], y + move[m_idx][1]
        dfs(nx, ny, new_path, m_idx)

        # 꺾는 경우
        if m_idx < 3:
            nx, ny = x + move[m_idx + 1][0], y + move[m_idx + 1][1]
            dfs(nx, ny, new_path, m_idx + 1) # m_idx + 1 로 방향전환


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    cnt = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)

    print(f'#{t} {cnt}')
