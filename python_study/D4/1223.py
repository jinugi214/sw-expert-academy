rank = {'*': 2, '+': 1}

for t in range(1, 11):

    _ = input()
    infix = input()

    stack = []
    postfix = []

# 중위표기식에서 후위 표기식으로 변환
    for i in infix:
        if not stack and i in ['+', '*']:
            stack.append(i)
        elif stack and i in ['+', '*']:
            tmp = stack.pop()
            if rank[i] > rank[tmp]:
                stack.append(tmp)
                stack.append(i)
            else:
                postfix += tmp
                stack.append(i)
        else:
            postfix += i

    else:
        while stack:
            postfix += stack.pop()

    nums = []

    for i in postfix:
        if i == '+':
            b = nums.pop()
            a = nums.pop()
            nums.append(a + b)

        elif i == '*':
            b = nums.pop()
            a = nums.pop()
            nums.append(a * b)

        else:
            nums.append(int(i))

    print(f'#{t} {nums[0]}')