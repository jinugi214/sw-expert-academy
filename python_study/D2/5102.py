def bfs(start):
    used = [0] * (V + 1)

    q = [(start, 0)]

    while q:

        x, cnt = q.pop(0)

        if x == G:
            return cnt

        for i in graph[x]:
            if not used[i]:
                q.append((i, cnt + 1))
                used[i] = 1

    return 0

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())

    ans = bfs(S)

    print(f'#{t} {ans}')
