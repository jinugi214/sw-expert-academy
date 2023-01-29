n = int(input())

for i in range(1, n+1):
    num = str(i)
    cnt = 0
    for j in num:
        if int(j) % 3 == 0 and int(j) > 0:
            cnt += 1

    if cnt == 0:
        print(num, end=' ')
    if cnt > 0:
        print('-'*cnt, end=' ')

