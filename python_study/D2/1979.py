# title : 어디에 단어가 들어갈 수 있을까?

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:      # 단어를 넣을 수 있다면
                cnt += 1
            else:           # 칸 없음!
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # 편하게 하기 위해서 양 옆과 밑에 0을 1칸씩 더 달아준다.
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]

    # arr(행)와 arr_t(열)로 각각 개수를 계산
    # 열은 전치행렬을 사용
    arr_t = list(zip(*arr))
    ans = count(arr) + count(arr_t)

    print(f'#{test_case} {ans}')