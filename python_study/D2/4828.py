T = int(input())

for t in range(1, T+1):
    n = int(input())

    nums = list(map(int, input().split())) # 값 입력

    # 최대값 찾기
    max_tmp = 0
    for num in nums:
        if num > max_tmp:
            max_tmp = num

    # 최솟값 찾기
    min_tmp = 1e9
    for num in nums:
        if num < min_tmp:
            min_tmp = num

    ans = max_tmp - min_tmp

    print(f'#{t} {ans}')