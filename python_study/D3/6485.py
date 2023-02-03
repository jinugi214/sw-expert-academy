T = int(input())

for t in range(1, T+1):
    n = int(input())
    route = []
    for _ in range(n):
        a, b = map(int, input().split())
        route.append([a, b])
    p = int(input())
    station = []
    for i in range(p):
        station.append(int(input()))

    print(f'#{t}', end=' ')
    for st in station:
        cnt = 0
        for rt in route:
            a, b = rt
            if a <= st <= b:
                cnt += 1
        print(cnt, end=' ')
    print()