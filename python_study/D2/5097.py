from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    nums = list(map(int, input().split()))

    data = deque(nums)

    for _ in range(M):
        data.append(data.popleft())

    print(f'#{t} {data[0]}')