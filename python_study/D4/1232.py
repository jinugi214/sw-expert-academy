def inorder(T):
    if len(node[T]) > 1:  # 번호와 연산자, 왼쪽 오른쪽 값이 있으면
        if node[T][0] == '+':
            return int(inorder(node[T][1])) + int(inorder(node[T][2]))
        elif node[T][0] == '-':
            return int(inorder(node[T][1])) - int(inorder(node[T][2]))
        elif node[T][0] == '*':
            return int(inorder(node[T][1])) * int(inorder(node[T][2]))
        elif node[T][0] == '/':
            return int(inorder(node[T][1])) // int(inorder(node[T][2]))
    if len(node[T]) == 1:  # 번호와 값만 있으면
        return node[T][0]  # 값 반환


for t in range(1, 11):
    N = int(input())

    node = {}  # 딕셔너리 사용
    # 정점 정수면 정점 번호와 양의 정수
    # 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽자식, 오른쪽 자식의 정점 번호
    for _ in range(N):
        key, *data = input().split()
        node[key] = data  # 각 키값에 값 담기

    print(f'#{t} {inorder("1")}')