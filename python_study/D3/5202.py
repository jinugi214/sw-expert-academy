T = int(input())


def dfs(si, e, cnt):
    for i in range(si+1, N):
        ns, ne = time[i]
        if ns >= e:
            dfs(i, ne, cnt + 1)
    else:
        global ans
        if ans < cnt:
            ans = cnt
        return


for t in range(1, T + 1):

    time = []

    # 신청서 수 N
    N = int(input())
    for _ in range(N):
        # 화물차 작업 시작시간 s, 종료시간 e
        s, e = map(int, input().split())
        time.append((s, e))
    time.sort()

    ans = 0
    for i in range(N):
        dfs(i, time[i][1], 1)

    print(f'#{t} {ans}')
