T = int(input())

for t in range(1, T+1):
    data = list(input())

    rlt = []

    rlt.append(data.pop())

    while data:
        val = data.pop()

        if rlt and rlt[-1] != val:
            rlt.append(val)
        elif rlt and rlt[-1] == val:
            rlt.pop()
        else:
            rlt.append(val)

    print(f'#{t} {len(rlt)}')