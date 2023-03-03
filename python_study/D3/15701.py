# 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체
import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    data_t = list(zip(*data)) # 전치행렬
    ans = 0
    for lst in data_t:
        prev = 0
        for n in lst:
            if n != 0:
                if n == 2 and prev == 1:
                    ans += 1
                prev = n
    # 위에 N극
    # 아래 S극
    print(f'#{t} {ans}')