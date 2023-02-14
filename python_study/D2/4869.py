def paper(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return paper(n - 10) + 2 * paper(n-20)

# 10 = 1

# 20 = 3

# 30 = 5

# 40 = 11


T = int(input())

for t in range(1, T+1):
    n = int(input())
    print(f'#{t} {paper(n)}')
