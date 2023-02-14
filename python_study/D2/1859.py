T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    # 최대값 찾아서 최대값 전에 최대값보다 작은 가격은 다 사기
    # 최대값 만나면 다 팔아버리기 그리고 그 이후 최대값 찾기하며 반복

    max_v = max(data)
    max_idx = 0

    rlt = 0
    cnt = 0
    price = 0
    for i in data:
        if i == max_v:
            rlt += i * cnt - price
            if len(data) - max_idx > 1 and len(data) :
                max_idx = data.index(max_v)  
                print(data[max_idx+1:len(data)])
                max_v = max(data[max_idx+1:len(data)])
        else:
            cnt += 1
            price += i
    
    print(f'#{t} {rlt}')