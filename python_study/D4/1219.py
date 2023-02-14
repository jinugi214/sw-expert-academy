def dfs(graph, v, visited):
    global ans
    if ans:
        return

    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            if i == B:
                ans = 1
                return
            dfs(graph, i, visited)

A = 0
B = 99

for _ in range(10):
    t, n = map(int, input().split())

    data = list(map(int, input().split()))

    graph = [[] * 100 for _ in range(100)]

    visited = [0] * 100

    for i in range(0, n * 2, 2):
        a, b = data[i], data[i + 1]
        graph[a].append(b)

    ans = 0

    dfs(graph, A, visited)

    print(f'#{t} {ans}')