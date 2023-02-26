'''
from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    nums = list(map(int, input().split()))

    data = deque(nums)

    for _ in range(M):
        data.append(data.popleft())

    print(f'#{t} {data[0]}')
'''

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))

    for _ in range(M):
        N_lst.append(N_lst.pop(0))

    print(f'#{t} {N_lst[0]}')