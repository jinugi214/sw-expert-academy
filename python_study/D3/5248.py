# 그룹나누기

# find_set 연산은 특정 노드에서 루트까지의 경로를 찾아가면서 노드의 부모정보를 갱신한다.
def find_set(x):
    if x == arr[x]:
        return arr[x]
    else:
        return find_set(arr[x])


# x와 y를 포함하는 두 집합을 통합하는 오퍼레이션
def union(x, y):
    rlt = find_set(y)
    for i in range(N + 1):
        if arr[i] == rlt:
            arr[i] = find_set(x)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [i for i in range(N + 1)]
    for i in range(0, M * 2, 2):
        # 같은 조로 연결해주기
        union(data[i], data[i + 1])
    # 조 개수 확인
    print(f'#{t} {len(set(arr)) - 1}')