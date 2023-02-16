for t in range(1, 11):

    _ = input()
    infix = input()

    stack = []
    postfix = []

# 중위표기식에서 후위 표기식으로 변환
    for i in infix:
        if i.isdigit(): # 숫자 확인
            postfix += i
        else:
            if i == '(': # ( '는 우선순위가 제일 높기 때문에 무조건 stack에 추가
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(': # top이 +보다 우선순위가 작을 때까지 pop
                    postfix += stack.pop()
                stack.append(i) # top이 '('이면 연산자 바로 추가
            elif i == '*': # * 는 + 보다 우선순위가 높기 때문에 스택에 * 를 추가
                while stack and stack[-1] == '*':
                    postfix += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(': # ) 은 ( 이 나올 때까지 스택을 계속 pop한다.
                    postfix += stack.pop()
                stack.pop()
    else:
        while stack: # 스택에 남은 연산자 모두 pop
            postfix += stack.pop()

# 후위표기식에서 계산
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