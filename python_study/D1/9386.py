T = int(input())

for t in range(1, T+1):
    n = int(input())
    per = list(map(int, input()))

    cnt_list = []
    cnt = 0
    prev = 0

    for i in range(n):
        if per[i] == 1 and prev == 0:
            cnt = 1
            prev = 1
        elif per[i] == 1 and prev == 1:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 0
    cnt_list.append(cnt)

    ans = cnt_list[0]
    for i in cnt_list:
        if ans < i:
            ans = i

    print(f'#{t} {ans}')