for t in range(1, 11):

    size = int(input())

    table = []

    for i in range(size):
        table.append(list(map(int, input().split())))

    cnt = 0

    for y in range(100):
        n = False
        for x in range(100):
            if table[x][y] == 1:
                n = True
            if table[x][y] == 2 and n == True:
                cnt += 1
                n = False

    print(f'#{t} {cnt}')
