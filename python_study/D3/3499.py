T = int(input())

for t in range(1, T + 1):
    N = int(input())

    card = list(input().split())

    rlt = []
    if N % 2 == 0:
        start = N // 2
        card1 = card[:start]
        card2 = card[start:]
        rlt.append(card1.pop(0))
        for i in range(len(card1)):
            rlt.append(card2[i])
            rlt.append(card1[i])

        rlt.append(card2[-1])
        rlt = ' '.join(rlt)
        print(f'#{t} {rlt}')

    else:
        start = N // 2 + 1
        card1 = card[:start]
        card2 = card[start:]
        for i in range(len(card2)):
            rlt.append(card1[i])
            rlt.append(card2[i])

        rlt.append(card1[-1])
        rlt = ' '.join(rlt)
        print(f'#{t} {rlt}')
