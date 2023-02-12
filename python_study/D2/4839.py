# title: 이진탐색

def binarySearch(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        middle = int((start + end) / 2)
        cnt += 1
        if middle == key:
            return cnt
        elif middle < key:
            start = middle
        elif middle > key:
            end = middle

T = int(input())

for t in range(1, T+1):
    p, a, b = map(int, input().split())
    a_cnt = binarySearch(p, a)
    b_cnt = binarySearch(p, b)

    if a_cnt < b_cnt:
        ans = 'A'
    elif a_cnt > b_cnt:
        ans = 'B'
    elif a_cnt == b_cnt:
        ans = 0

    print(f'#{t} {ans}')

