T = int(input())

for t in range(1, T + 1):
    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14

    error_check = False

    data = input()

    for i in range(0, len(data), 3):
        pattern = data[i]
        num = int(data[i + 1:i + 3])
        if pattern == 'S' and S[num] == 0:
            S[num] = 1
        elif pattern == 'D' and D[num] == 0:
            D[num] = 1
        elif pattern == 'H' and H[num] == 0:
            H[num] = 1
        elif pattern == 'C' and C[num] == 0:
            C[num] = 1
        else:
            print(f'#{t} ERROR')
            error_check = True
            break

    if error_check:
        continue

    s = 13 - sum(S)
    d = 13 - sum(D)
    h = 13 - sum(H)
    c = 13 - sum(C)

    print(f'#{t} {s} {d} {h} {c}')