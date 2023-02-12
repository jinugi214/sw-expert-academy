# title : 특별한 정렬

def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    return a

T = int(input())

for t in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    data = selectionSort(data, len(data))
    print(f'#{t}', end=' ')
    for i in range(5):
        print(data[-i-1], end=' ')
        print(data[i], end=' ')
    print()