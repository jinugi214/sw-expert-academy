dict = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
        }


# 7번째 숫자 모두 1이니까 이거 이용해서 암호코드 찾자
def find_password():
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if data[i][j] == '1':
                return i, j - 55  # 현재 포함 56개


T = int(input())

for t in range(1, T + 1):

    N, M = map(int, input().split())

    data = [list(input()) for _ in range(N)]

    x, y = find_password()
    password = ''
    for i in range(y, y + 56):
        password += data[x][i]

    ord_n = []
    even_n = []
    pwd = []
    for i in range(0, len(password), 7):
        tmp = ''.join(map(str, password[i:i + 7]))
        if (i + 1) % 2 == 0:
            even_n.append(dict[tmp])
        else:
            ord_n.append(dict[tmp])

    # 올바른 암호코드는 (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수
    val = sum(ord_n) * 3 + sum(even_n)
    if val % 10 == 0:
        ans = sum(ord_n) + sum(even_n)
    else:
        ans = 0

    print(f'#{t} {ans}')
