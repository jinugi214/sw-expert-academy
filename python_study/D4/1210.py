# title: Ladder1

for _ in range(1, 11):
    t = input()
    ladder = []

    for i in range(100):
        ladder.append(list(map(int, input().split())))

    x, y = 0, 0
    for i in range(100):
        if ladder[99][i] == 2:
            x, y = 99, i
            break

    while True:
        if x == 0:
            break
        if 0 < y < 100 and ladder[x][y-1] == 1:
            ladder[x][y] = 0
            x, y = x, y-1
        elif 0 <= y < 99 and ladder[x][y+1] == 1:
            ladder[x][y] = 0
            x, y = x, y+1
        else:
            ladder[x][y] = 0
            x, y = x-1, y
    print(f'#{t} {y}')
