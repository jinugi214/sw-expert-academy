T = int(input())

def dfs(x, y, val):

    global ans
    if x == N-1 and y == N-1:
        if val < ans:
            ans = val
        return


    for dx, dy in ((1, 0), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, val + data[nx][ny])


for t in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for i in range(N)]

    ans = 1e9
    dfs(0, 0, data[0][0])

    print(f'#{t} {ans}')