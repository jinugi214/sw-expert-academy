T = int(input())

for t in range(1, T+1):
    n = int(input())

    cnt = [0] * 10

    nums = input()

    for i in nums:
        cnt[int(i)] += 1

    ans_cnt = 0
    ans_num = 0

    for i in range(1, len(cnt)):
        if cnt[i] > ans_cnt:
            ans_num = i
            ans_cnt = cnt[i]
        elif cnt[i] == ans_cnt:
            if ans_num < i:
                ans_num = i

    print(f'#{t} {ans_num} {ans_cnt}')