for t in range(1, 11):

    N, data = input().split()

    data = list(map(int, data))

    stack = []

    for i in data:
        if stack and stack[-1] != i:
            stack.append(i)
        elif stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{t} {"".join(map(str, stack))}')
