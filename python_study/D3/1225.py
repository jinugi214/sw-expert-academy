for t in range(1, 11):
    _ = input()
    data = list(map(int, input().split()))
    i = 1
    while data[-1] != 0:

        val = data.pop(0) - i
        if val < 0:
            val = 0
        data.append(val)
        i += 1
        if i > 5:
            i = 1

    ans = ' '.join(map(str, data))
    print(f'#{t} {ans}')