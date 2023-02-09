# title: 회문1

def pali(word , n):
    if n == 1:
        return True
    else:
        half = len(word) // 2
        front = []
        back = []
        for i in range(half):
            front.append(word[i])
            back.append(word[-(i+1)])
        if front == back:
            return True
        else:
            return False


for t in range(1, 11):
    n = int(input())
    data = []
    for _ in range(8):
        data.append(list(input()))
    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            if pali(data[i:n], n):
                cnt += 1

    for i in range(8):
        for j in range(8 - n + 1):
            col = []
            for k in range(n):
                col.append(data[j+k][i])

            if pali(col, n):
                cnt += 1

    print(f'#{t} {cnt}')