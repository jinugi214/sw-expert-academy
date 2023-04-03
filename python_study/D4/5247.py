# 연산

from collections import deque

T = int(input())


def bfs(N):
    sset = set()
    q = deque()
    q.append((N, 0))

    while q:
        val, cnt = q.popleft()
        if val >= 1000000:
            continue
        cnt += 1
        for i in range(4):
            if i == 0:
                if val + 1 not in sset:
                    q.append((val + 1, cnt))
                    sset.add(val + 1)
                    if val + 1 == M:
                        return cnt
            elif i == 1:
                if val - 1 not in sset:
                    q.append((val - 1, cnt))
                    sset.add(val - 1)
                    if val - 1 == M:
                        return cnt
            elif i == 2:
                if val * 2 not in sset:
                    q.append((val * 2, cnt))
                    sset.add(val * 2)
                    if val * 2 == M:
                        return cnt
            elif i == 3:
                if val - 10 not in sset:
                    q.append((val - 10, cnt))
                    sset.add(val - 10)
                    if val - 10 == M:
                        return cnt


for t in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{t} {bfs(N)}')