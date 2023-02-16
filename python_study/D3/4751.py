T = int(input())

for t in range(1, T+1):
    text = list(input())

    top1 = '.#..'
    top2 = '#.#.'
    mid1, mid2 = '.', '.#'
    btm2 = '#.#.'
    btm1 = '.#..'

    top1_lst = ['.']
    top2_lst = ['.']
    mid_lst = ['#']
    btm2_lst = ['.']
    btm1_lst = ['.']

    for a in text:
        top1_lst.append(top1)
        top2_lst.append(top2)
        mid_lst.append(mid1)
        mid_lst.append(a)
        mid_lst.append(mid2)
        btm2_lst.append(btm2)
        btm1_lst.append(btm1)

    print(''.join(top1_lst))
    print(''.join(top2_lst))
    print(''.join(mid_lst))
    print(''.join(btm2_lst))
    print(''.join(btm1_lst))