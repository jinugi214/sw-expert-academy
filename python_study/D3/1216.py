# title: 회문2

N = M = 100

for t in range(1, 11):
    _ = int(input())
    data = [list(input()) for _ in range(N)]

    pali_len = 0
    for i in range(N):
        for j in range(M):
            for k in range(M - j + 1):
                for l in range(j // 2):
                    if data[i][k + l] != data[i][k + j - 1 - l]:
                        break
                else:
                    if j > pali_len:
                        pali_len = j

    for i in range(N):
        for j in range(M):
            for k in range(M - j + 1):
                for l in range(j // 2):
                    if data[k + l][i] != data[k + j - 1 - l][i]:
                        break
                else:
                    if j > pali_len:
                        pali_len = j

    print(f'#{t} {pali_len}')