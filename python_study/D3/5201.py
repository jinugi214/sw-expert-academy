T = int(input())
# 화물을 싣지 못한 트럭이 있을 수도 있고
# 화물이 있을 수도 있다.
# 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력
for t in range(1, T+1):
    # 컨테이너수 N, 트럭수 M
    N, M = map(int, input().split())
    # 컨테이너마다 실린 화물 무게
    con = list(map(int, input().split()))
    # 트럭마다의 적재용량
    truck = list(map(int, input().split()))

    con.sort()
    truck.sort()

    ans = 0

    while True:
        if not truck or not con:
            break
        for i in range(1, len(con)+1):
            if con[-i] <= truck[-1]:
                ans += con.pop(-i)
                truck.pop()
                break
        else:
            break
    print(f'#{t} {ans}')