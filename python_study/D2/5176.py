# 왼쪽 서브트리의 루트 -> 현재 노드 ->오른쪽 서브 트리의 루트인 규칙 => 중위 순회
def inorder(T):
    global num # 입력할 값
    if T > N: # 현재 노드가 N보다 크면
        return
    inorder(T*2) # 재귀로 왼쪽값들 먼저 입력
    tree[T] = num
    num += 1 # 입력하고 나서 += 1
    inorder(T*2 + 1) # 재귀로 오른쪽값들 입력


test_case = int(input())

for t in range(1, test_case+1):
    N = int(input())
    tree = [0] * (N+1) # 이진 트리
    num = 1 # 이진트리에 저장할 값
    inorder(1) # 이진트리 탐색 시작
    print(f'#{t} {tree[1]} {tree[N//2]}') # 루트 값과 N//2 노드 출력 (소수점을 버리기 위해)