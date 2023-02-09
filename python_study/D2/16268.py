# title: 풍선팡2

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    dx = [0, 0, 1, -1] # 동서남북
    dy = [1, -1, 0, 0]

    max_val = 0

    for x in range(n):
        for y in range(m):
            val = 0
            val += data[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    val += data[nx][ny]
            if val > max_val:
                max_val = val
    print(f'#{t} {max_val}')
