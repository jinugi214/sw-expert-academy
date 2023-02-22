def inorder(T):  # 중위순회
    if chars[T] == '': # 문자 없으면 반환
        return
    inorder(tree[0][T]) # 왼쪽 먼저
    print(chars[T], end='')
    inorder(tree[1][T]) # 그다움 오른쪽


for t in range(1, 11):
    N = int(input())

    chars = [''] * (N + 1) # 문자 담는 곳
    tree = [[0] * (N + 1) for _ in range(2)] # 트리만들기
    for _ in range(N):
        data = input().split() # 입력 받기
        num = int(data[0])
        chars[num] = data[1] # 각 노드에 문자 넣어주기
        if len(data) > 2: # 왼쪽트리 입력받을 경우
            tree[0][num] = int(data[2])
        if len(data) > 3: # 오른쪽트리도 입력받는 경우
            tree[1][num] = int(data[3])

    print(f'#{t}', end=' ')
    inorder(1)
    print()
