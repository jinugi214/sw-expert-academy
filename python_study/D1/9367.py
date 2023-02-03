T = int(input())

for t in range(1, T+1):

    n = int(input())

    carrot = list(map(int, input().split()))

    cnt_list = []
    cnt = 1
    for i in range(1, len(carrot)):
        if carrot[i] == carrot[i-1] + 1:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1
    cnt_list.append(cnt)

    ans = cnt_list[0]
    for i in cnt_list:
        if ans < i:
            ans = i

    print(f'#{t} {ans}')