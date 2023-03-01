# 암호코드들이 붙어있는 경우는 존재하지 않는다.
# (각 암호코드의 둘레에는 최소 1칸 이상의 빈 공간이 존재한다.)
import sys

sys.stdin = open('sample_input.txt')

code = {(3, 2, 1, 1): 0,
        (2, 2, 2, 1): 1,
        (2, 1, 2, 2): 2,
        (1, 4, 1, 1): 3,
        (1, 1, 3, 2): 4,
        (1, 2, 3, 1): 5,
        (1, 1, 1, 4): 6,
        (1, 3, 1, 2): 7,
        (1, 2, 1, 3): 8,
        (3, 1, 1, 2): 9  # 1이었던 값이 나중에 몇배 늘어난지 배수가 된다.
        }


# 16진수 한 자리 수를 2진수 네자리 수로 변경
def hex_to_binary(n):
    # 10진수로 변경해서 2진수로 변경
    n = int(n, 16)  # 10진수로 변경하기
    result = ''
    exp = 3
    while n > 0:
        if n >= 2 ** exp:
            result += '1'
            n -= 2 ** exp
        else:
            result += '0'
        exp -= 1

    while len(result) < 4:
        result += '0'
    return result


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    data = [input() for _ in range(N)]
    bin_data = []

    # 16진수 문자열들을 전부 2진수 문자열로 바꿔준다.
    for i in range(N):
        bin_line = ''
        for j in range(M):
            bin_line += hex_to_binary(data[i][j])
        bin_data.append(bin_line)
    data = bin_data

    # 뒤에서부터 1찾기
    ans = 0
    for i in range(1, N):
        idx = M * 4 - 1  # 2진수로 바꾸면서 길이가 4배 늘어났기에
        while idx > 54: # 2진수로 바꿨을 시 왼쪽 한계점
            if data[i - 1][idx] == '0' and data[i][idx] == '1':  # 위칸과 다른 값 => 첫 암호코드
                password = []
                for _ in range(8):
                    w1, w2, w3, w4 = 0, 0, 0, 0
                    while data[i][idx] == '1':
                        w4 += 1
                        idx -= 1
                    while data[i][idx] == '0':
                        w3 += 1
                        idx -= 1
                    while data[i][idx] == '1':
                        w2 += 1
                        idx -= 1

                    # 암호코드 비율 찾아내기
                    rate = min(w2, w3, w4)
                    w2 //= rate
                    w3 //= rate
                    w4 //= rate
                    w1 = 7 - w2 - w3 - w4
                    idx -= w1 * rate  # w1만큼 idx 앞으로 이동
                    password.append(code[(w1, w2, w3, w4)])

                odd_n = password[1] + password[3] + password[5] + password[7]
                even_n = password[0] + password[2] + password[4] + password[6]

                if (odd_n * 3 + even_n) % 10 == 0: # 올바른 암호코드 검사
                    ans += (odd_n + even_n)

            idx -= 1 # 무한루프 탈출용 (다른 암호 찾으러)

    print(f'#{t} {ans}')
