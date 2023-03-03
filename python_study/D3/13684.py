T = int(input())

for t in range(1, T + 1):

    data = [list(input()) for _ in range(5)]

    ans = ''

    for i in range(len(data[0])):
        for j in range(5):
            try:
                ans += data[j][i]
            except IndexError:
                continue
    print(f'#{t} {ans}')