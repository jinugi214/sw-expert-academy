# bfs 완전탐색

# 운영 비용 = K * K + (K - 1) * (K - 1)
# 이익 = M * 집수 - 운영 비용

# # 운영비용 손해보지 않으면 최대 집 개수 갱신
def renew(home, k_cost):
    global max_cnt
    if M * home - k_lst[k_cost] >= 0:
        max_cnt = max(home, max_cnt)


def bfs(sx, sy):
    q = [(sx, sy)]
    visit = [[0] * N for _ in range(N)]
    visit[sx][sy] = 1

    home = data[sx][sy]
    k_cost = 1  # 시작점 비용 포함

    renew(home, k_cost)  # 1일 때도 검사

    while k_cost < N + 2:  # 지역 N+1 까지 (모든 지역을 포함할 때까지)
        for _ in range(len(q)):
            x, y = q.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy  # 4방향 이동
                if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:  # 범위, 방문 확인
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                    if data[nx][ny]:  # 집이 있으면
                        home += 1  # 집 추가
        k_cost += 1  # 마름모가 커지므로 K 증가
        renew(home, k_cost) # 값 검사


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 도시의 정보에서 집이 있는 위치는 1이고, 나머지는 0이다.
    # 도시에는 최소 1개 이상의 집이 존재한다.
    data = [list(map(int, input().split())) for _ in range(N)]

    # 최종 집 수
    max_cnt = 0

    # 비용은 항상 동일하기 때문에 미리 구해두기
    k_lst = [k * k + (k - 1) * (k - 1) for k in range(26)]  # k 값 리스트

    for i in range(N):
        for j in range(N):
            bfs(i, j) # 모든 곳 검사해보기

    print(f'#{t} {max_cnt}')
