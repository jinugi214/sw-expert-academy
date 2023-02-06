A = [i for i in range(1, 13)]

T = int(input())


def sum_list(check_list):
    val = 0
    for i in check_list:
        val += i
    return val


for t in range(1, T + 1):

    n, k = map(int, input().split())

    ans_cnt = 0

    for i in range(1 << len(A)):

        tmp_cnt = 0
        tmp_value = 0
        for j in range(len(A)):
            if i & (1 << j):
                tmp_cnt += 1
                tmp_value += A[j]
        if tmp_cnt == n and tmp_value == k:
            ans_cnt += 1

    print(f'#{t} {ans_cnt}')