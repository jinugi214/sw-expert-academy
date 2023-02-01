T = int(input())

for t in range(1, T+1):

    n, m = map(int, input().split())

    nums = list(map(int, input().split()))

    max_val = 0
    min_val = 1e9
    for i in range(n - m + 1):
        val = 0
        for j in range(i, i+m):
            val += nums[j]
        if max_val < val:
            max_val = val

        if min_val > val:
            min_val = val

    ans = max_val - min_val

    print(f'#{t} {ans}')