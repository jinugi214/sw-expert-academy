import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작노드의 최단 거리는 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는 값이 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())

    graph = [[] for i in range(N+1)]

    # 최단거리 테이블
    distance = [1e9] * (N + 1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    # 다익스트라 실행
    dijkstra(0)

    print(f'#{t} {distance[N]}')