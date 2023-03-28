T = int(input())


def check(arr):
    for i in range(len(arr)):
        if arr[i] >= 3:
            return True
        if i < 8 and arr[i] and arr[i + 1] and arr[i + 2]:
            return True


for t in range(1, T + 1):
    card = list(map(int, input().split()))
    a = [0] * 10
    b = [0] * 10
    ans = 0
    for i in range(0, 12, 2):
        a[card[i]] += 1
        if check(a):
            ans = 1
            break
        b[card[i + 1]] += 1
        if check(b):
            ans = 2
            break
    print(f'#{t} {ans}')
