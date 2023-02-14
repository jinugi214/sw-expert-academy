T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    rlt = 0
    max_num = 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] > max_num:
            max_num = data[i]
        else:
            rlt += max_num - data[i]

    print(f'#{t} {rlt}')