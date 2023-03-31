# 부분 수열의 합

T = int(input())


def dfs(n, sm):
    global ans
    # 가지치기
    if K < sm:
        return


    # 종료조건
    if n == N:
        if sm == K:
            ans += 1
        return

    # 하부호출
    dfs(n+1, sm+lst[n]) # 포함
    dfs(n+1, sm)

for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)

    print(f'#{t} {ans}')