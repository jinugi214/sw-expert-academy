def divide(start, end):
    if start == end:
        return start

    a = divide(start, (start + end) // 2)
    b = divide((start + end) // 2 + 1, end)
    return rps(a, b)


def rps(a, b):
    if card[a] == card[b]:
        return a
    elif card[a] == 1:
        if card[b] == 2:
            return b
        elif card[b] == 3:
            return a
    elif card[a] == 2:
        if card[b] == 1:
            return a
        elif card[b] == 3:
            return b
    elif card[a] == 3:
        if card[b] == 2:
            return a
        elif card[b] == 1:
            return b

T = int(input())

for t in range(1, T+1):

    N = int(input())

    card = list(map(int, input().split()))

    print(f'#{t} {divide(0, N-1)+1}')