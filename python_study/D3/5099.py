'''
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
'''

# 2차 풀이
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기 N과 피자 개수 M
    all_pizza = list(map(int, input().split()))

    oven = []
    pizza = []

    for idx, cheese in enumerate(all_pizza):
        pizza.append([cheese, idx + 1])

    for i in range(N):
        oven.append(pizza.pop(0))

    while len(oven) > 1:
        if len(oven) < N and pizza:
            oven.append(pizza.pop(0))
        cheese, num = oven.pop(0)
        cheese //= 2
        if cheese == 0:
            continue
        else:
            oven.append([cheese, num])
    print(f'#{t} {oven[0][1]}')
