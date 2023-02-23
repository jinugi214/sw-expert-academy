def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return

def check_par(n):
    if n == 1:
        return
    n = n // 2
    global ans
    ans += heap[n]
    check_par(n)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0

    for i in data:
        enq(i)
    ans = 0
    check_par(last)

    print(f'#{t} {ans}')