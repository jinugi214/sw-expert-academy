T = 10

for test_case in range(1, T+1):
    # 의미없는 숫자 입력이라서
    _ = int(input())
    # 편하게 하기 위해 양 옆에 0을 한칸씩 받아준다.
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100*100
    for y in range(1, 101): # 양옆 0넣어준 것 때문에 인덱스 1~100
        x, cnt, dj = 0, 0, 0 # x와, 횟수, 방향
        # 시작점 찾기
        if arr[x][y] != 1:
            continue
        dx, dy = x, y
        while dx < 99: # 99도착하면 멈추기
            cnt += 1 # 횟수 추가
            if dj == 0: # 진행방향 아래인 경우
                if arr[dx][dy-1] == 1: # 좌측 확인
                    dj = -1
                    dy -= 1
                elif arr[dx][dy+1] == 1: # 우측 확인
                    dj = 1
                    dy += 1
                else:
                    dx += 1
            else:
                if arr[dx][dy+dj] == 1: # 좌, 우에 1이 더 있으면 더 진행
                    dy += dj
                else: # 진행방향이 막힌 경우 아래로
                    dj = 0
                    dx += 1

        # 최단거리 확인과 시작한 출발점 받기
        if mn >= cnt:
            mn, ans = cnt, y-1

    print(f'#{test_case} {ans}')