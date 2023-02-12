T = int(input())

def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


for t in range(1, T+1):
    n = int(input())

    nums = list(map(int, input().split())) # 값 입력

    data = BubbleSort(nums)

    ans = data[-1] - data[0]

    print(f'#{t} {ans}')