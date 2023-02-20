arr = [1, 2, 3, 4, 5]
N = len(arr)
selected = [0] * N
K = 3 # 구할 개수

# idx번째 요소를 조합에 포함할지 안할지 결정

# cnt = 여태까지 선택한 요소의 개수
def comb(idx, cnt):
    if cnt == K:
        print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i], end=' ')
        print()
        return
    if idx == N: # 마지막 인덱스까지 모두 결정했으나 K를 선택하지 못함
        return

    for i in range(2):
        selected[idx] = i
        comb(idx + 1, cnt+1 * i)
        selected[idx] = 0

comb(0, 0)