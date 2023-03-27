T = int(input())

def dfs(x, val):
    global ans
    if sum(used) == N:
        if val < ans:
            ans = val
        return

    for i in range(1, N+1):
        if data[x][i] and not used[i]:
            if sum(used) != N-1 and i == 1:
                continue
            else:
                used[i] = 1
                # print(x)
                dfs(i, val+data[x][i])
                used[i] = 0

for t in range(1, T+1):
    N = int(input())

    data = [[0]*(N+1)]+[[0] + list(map(int, input().split())) for _ in range(N)]
    # 최소소비량 계산하기
    ans = 1e9

    used = [0] * (N + 1)
    dfs(1, 0)

    print(f'#{t} {ans}')