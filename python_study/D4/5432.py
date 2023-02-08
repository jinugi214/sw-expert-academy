# title : 쇠막대기

T = int(input())

for t in range(1, T+1):
    data = list(input())

    # 막대기 계속 계산해주기
    # 레이저 나오면 왼쪽 막대기 개수만 더해주기
    # 막대기 끝나면 끝난 막대기 개수만큼 더해주기

    stick = 0
    rlt = 0
    for i in range(len(data)):
        if data[i] == '(' and data[i+1] == ')': # 레이저
            rlt += stick
        elif data[i] == '(': # 쇠막대기 시작
            stick += 1
        elif data[i] == ')' and data[i-1] != '(': # 쇠막대기 끝
            stick -= 1
            rlt += 1

    print(f'#{t} {rlt}')