def dfs(graph, v, visited):
    global check
    if check:
        return

    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            if i == G:
                check = 1
                return
            dfs(graph, i, visited)


T = int(input())

for t in range(1, T+1): # V는 노드개수 # E는 간선개수
    V, E = map(int, input().split())

    graph = [[] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    S, G = map(int, input().split())

    visited = [0] * (V + 1)

    check = 0

    dfs(graph, S, visited)

    print(f'#{t} {check}')
