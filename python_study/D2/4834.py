T = int(input())


for t in range(1, T+1):

    N = int(input())

    card = list(map(int, input()))

    card_cnt = [0] * 10

    for i in card:
        card_cnt[i] += 1

    card_num = 0
    cnt = 0
    for i in range(len(card_cnt)):
        if card_cnt[i] > cnt:
            card_num = i
            cnt = card_cnt[i]
        elif card_cnt[i] == cnt:
            card_num = i

    print(f'#{t} {card_num} {cnt}')
