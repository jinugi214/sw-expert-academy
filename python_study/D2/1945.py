T = int(input())

for t in range(1, T + 1):
    n = int(input())
    nums = [0] * 12

    div = [2, 3, 5, 7, 11]

    while True:
        if n == 1:
            break
        for i in div:
            if n % i == 0:
                nums[i] += 1
                n /= i

    print(f'#{t}', end=' ')
    for i in div:
        print(f'{nums[i]}', end=' ')
    print()
