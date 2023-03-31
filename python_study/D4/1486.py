# 장훈이의 높은 선반

def dfs(n, sm):

    global ans
    if ans == 0: # 바로 정답!
        return

    if n == N:
        if sm >= B:
            ans = min(ans, sm - B)
        return

    dfs(n + 1, sm + lst[n])  # 포함
    dfs(n + 1, sm)  # 미포함


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N * 10000
    dfs(0, 0)

    print(f'#{test_case} {ans}')