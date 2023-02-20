from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    Ci = list(map(int, input().split()))

    p_idx = deque([x for x in range(M)])
    pizza = deque(Ci)
    idx = deque()
    q = deque()
    for i in range(N):
        q.append(pizza.popleft())
        idx.append(p_idx.popleft())

    while len(idx) != 1:
        val = q.popleft()
        idx_t = idx.popleft()
        if val == 1:
            if len(pizza) > 0:
                q.append(pizza.popleft())
                idx.append(p_idx.popleft())
        else:
            q.append(val // 2)
            idx.append(idx_t)

    print(f'#{t} {idx[0]+1}')
