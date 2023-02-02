T = int(input())

# k는 한번 충전으로 최대 이동 수
# n은 0 ~ n번 종점 정류장 번호
# m은 충전소 개수
for t in range(1, T+1):
    k, n, m = map(int, input().split())
    charger = list(map(int, input().split()))

    cnt = 0
    bus = 0
    prev = 0
    check = True
    while check:
        bus += k
        if bus >= n:
            break
        for i in range(m - 1, -1, -1):
            if bus >= charger[i]:
                cnt += 1
                bus = charger[i]
                if prev == bus:
                    check = False
                    cnt = 0
                    break
                else:
                    prev = bus
                    break

    print(f'#{t} {cnt}')
