# 수영장

def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n > 12:
        ans = min(ans, sm)
        return

    dfs(n + 1, sm + day * lst[n])  # 일간권
    dfs(n + 1, sm + mon)  # 월
    dfs(n + 3, sm + mon3)  # 분기권
    dfs(n + 12, sm + year)  # 년간


T = int(input())
for test_case in range(1, T + 1):
    # 1일 이용권, 1달 이용권, 3달 이용권, 1년 이용권의 요금
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    ans = 365 * 3000 # 나올 수 있는 가장 큰 값을 임시로 둔다.
    dfs(1, 0)

    # 이용 계획대로 수영장을 이용하는 경우 중 가장 적게 지출하는 비용
    print(f'#{test_case} {ans}')