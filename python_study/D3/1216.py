# title: 회문2

def pali(word):
    half = len(word) // 2  # 회문을 검사하기 위해 리스트를 반으로 쪼개기
    for i in range(half):  # 문자를 앞과 뒤를 하나씩 확인
        if word[i] != word[-(i + 1)]:  # 단어가 서로 다를시에
            return False
    return True  # 다 검사해도 이상없을시에 True 반환

m = 100

for t in range(1, 11):
    _ = int(input())
    data = [list(input()) for _ in range(m)]

    pali_len = 0

    for i in range(m): # 열 0~99
        for j in range(m): # 행 0 ~ 99
            brk = False
            for k in range(m-1, j-1, -1): # 행 역순 검사 최대 길이 순회
                for l in range(j, k+1 // 2): # 행 현재 최대 길이 안에서 반복
                    if data[i][l] != data[i][-(l+1)]:
                        break
                brk = True
                if k - j > pali_len:
                    pali_len = k - j
                if brk:
                    break

    data_t = list(zip(*data))

    for i in range(m):
        for j in range(m):
            brk = False
            for k in range(m - 1, j-1, -1):
                for l in range(j, k+1):
                    if data[i][l] != data[i][-(l + 1)]:
                        break
                brk = True
                if k - j > pali_len:
                    pali_len = k - j
                if brk:
                    break

    print(f'#{t} {pali_len}')