t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    data = list(map(int, input().split()))

    up_list = []

    for i in range(1, len(data)-1):
        for j in range(i + 1, len(data)-1):
            up_list.append(data[i] * data[j])

    ans_list = []
    for i in up_list:
        tmp = list(str(i))
        for j in range(1, len(tmp)):
            if tmp[j] < tmp[j - 1]:
                break
        else:
            ans_list.append(i)

    if len(ans_list) == 0:
        ans = -1
    else:
        ans = max(ans_list)

    print(f'#{test_case} {ans}')
