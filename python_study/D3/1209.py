for _ in range(10):
    t = input()

    data = []
    for i in range(100):
        data.append(list(map(int, input().split())))

    rlt = 0
    for i in range(100):
        row_val = 0
        for j in range(100):
            row_val += data[i][j]
        if row_val > rlt:
            rlt = row_val

    for i in range(100):
        column_val = 0
        for j in range(100):
            column_val += data[j][i]
        if column_val > rlt:
            rlt = column_val

    for i in range(100):
        dia_val = 0
        for j in range(i + 1, 100 - i):
            if i == j:
                dia_val += data[i][j]
            else:
                continue
        if dia_val > rlt:
            rlt = dia_val

    print(f'#{t} {rlt}')
