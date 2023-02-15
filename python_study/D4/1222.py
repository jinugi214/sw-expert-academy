for t in range(1, 11):
    _ = int(input()) # 의미 없는 입력
    data = list(input()) # 문자열 계산식 입력

    stack = [] # +연산자 담는 곳
    num = [] # 계산할 숫자들
    post = '' # 후위표기 문자열 받는 곳


    # --------후위표기식으로 바꾸자------
    for i in data:
        if not stack and i == '+': # 스택안에 비어있는데 + 연산자이면 그냥 담기
            stack.append(i)
        elif stack and i == '+': # 스택안에 +가 이미 들어있으면 뺴고 추가
            post += stack.pop() # 들어있는거 꺼내서 후위표기에 달기
            stack.append(i) # 연산자는 스택에 넣기
        else:
            post += i # 숫자는 후위표기에 달기

    else:
        post += stack.pop() # 데이터 순회 다 끝나면 스택안에 남은 + 꺼내서 후위표기 뒤에 달기


    # ------이제 후위표기식을 계산해서 값을 구하자-----
    for i in post:
        if i == '+': # + 연산자나오면
            b = num.pop()
            a = num.pop()
            num.append(a + b)

        elif i != '+': # + 연산자 아니면
            num.append(int(i))

    print(f'#{t} {num[0]}')
