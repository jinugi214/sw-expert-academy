for t in range(1, 11):
    n = int(input())
    dump = list(map(int, input().split()))

    for _ in range(n):
        min_val = dump[0]
        max_val = dump[0]
        min_idx = 0
        max_idx = 0
        for i in range(100):
            if min_val > dump[i]:
                min_val = dump[i]
                min_idx = i
            elif max_val < dump[i]:
                max_val = dump[i]
                max_idx = i
        dump[max_idx] -= 1
        dump[min_idx] += 1

    min_val = dump[0]
    max_val = dump[0]
    for i in dump:
        if min_val > i:
            min_val = i
        elif max_val < i:
            max_val = i

    ans = max_val - min_val
    print(f'#{t} {ans}')
