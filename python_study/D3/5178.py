T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드 개수, 리프 노드 개수, 출력한 노드 번호

    node = [0] * (N + 1)

    for _ in range(M):
        num, val = map(int, input().split())
        node[num] = val

    for i in range(N, 1, -1):
       node[i // 2] += node[i]

    print(f'#{t} {node[L]}')
