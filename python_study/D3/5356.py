# title: 의석이의 세로로 말해요

T = int(input())

for t in range(1, T+1):
    data = []
    for i in range(5):
        data.append(list(input()))

    max_len = 0
    for i in range(5):
        if len(data[i]) > max_len:
            max_len = len(data[i])

    for i in range(5):
        dif = max_len - len(data[i])
        if dif > 0:
            for _ in range(dif):
                data[i].append(' ')

    print(f'#{t}', end=' ')
    for i in range(max_len):
        for j in range(5):
            if data[j][i] == ' ':
                continue
            else:
                print(data[j][i], end='')
    print()