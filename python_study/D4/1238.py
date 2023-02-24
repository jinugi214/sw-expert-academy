def bfs(S):
    used = [0] * 101
    q = [S]
    used[S] = 1
    rlt = S

    while q:
        cur = q.pop(0)

        if used[rlt] < used[cur] or used[rlt] == used[cur] and rlt < cur:  # 이동횟수와 노드의 값 확인
            rlt = cur  # 현재 최대값 지정

        for i in node[cur]:
            if used[i] == 0:  # 한번도 안왔던 곳
                q.append(i)
                used[i] = used[cur] + 1  # 이동횟수 추가

    return rlt


for t in range(1, 11):
    N, S = map(int, input().split())
    node = [[] for _ in range(101)]
    data = list(map(int, input().split()))
    for i in range(0, N, 2):
        s = data[i]  # 이동 시작점
        e = data[i + 1]  # 이동 도착점
        node[s].append(e)

    print(f'#{t} {bfs(S)}')