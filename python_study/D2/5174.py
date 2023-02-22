def preorder(T):
    if T == 0:
        return 0
    return 1 + preorder(tree[T][0]) + preorder(tree[T][1])
    # 재귀할 때마다 +1 왼쪽과 오른쪽 노드 탐색

T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())  # N을 루트로 하는 서브 트리에 속한 노드 개수 E
    data = list(map(int, input().split()))  #

    tree = [[0] * 2 for _ in range(E + 2)]

    for i in range(0, E * 2, 2):  # 입력받은 간선 정보를 트리에 넣어줌
        if not tree[data[i]][0]:  # 왼쪽이 비어있다면
            tree[data[i]][0] = data[i + 1]
        else:  # 왼쪽이 있다면 오른쪽
            tree[data[i]][1] = data[i + 1]

    ans = preorder(N)  # 루트로 받아주는 N부터 찾음
    print(f'#{t} {ans}')