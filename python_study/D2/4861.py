# title : 회문

def pali(word): # word : 리스트화한 단어
    half = len(word) // 2 # 회문을 검사하기 위해 리스트를 반으로 쪼개기
    for i in range(half): # 문자를 앞과 뒤를 하나씩 확인
        if word[i] != word[-(i+1)]: # 단어가 서로 다를시에
            return False
    return True # 다 검사해도 이상없을시에 True 반환


T = int(input()) # 테스트케이스 입력

for t in range(1, T+1):
    n, m = map(int, input().split()) # 글자판 크기인 N과 회문길이인 M 입력
    data = []
    for _ in range(n): # 문자열을 입력
        data.append(list(input()))

    brk = False # 이중 for문 탈출을 위해 우선 False를 설정
    for i in range(n): # 행을 완전탐색으로 검사
        if brk: # break 확인
            break
        for j in range(n - m + 1): # 글자판 크기 - 문자길이 + 1
            if pali(data[i][j:j+m]):
                # 현재 인덱스에서 행으로 + 문자길이까지 슬라이싱
                # 함수에 넣은 회문 검사가 True이면
                ans = ''.join(data[i][j:m + j]) # 리스트 문자열로 변환
                print(f'#{t} {ans}') # 출력
                brk = True # 이중 for문 탈출을 위해 True 설정
                break

    for i in range(n): # 열을 완전탐색으로 검사
        if brk: # break 확인
            break
        for j in range(n - m + 1): # 글자판크기 - 문자길이 + 1
            col = [] # 문자들을 담아줄 리스트
            for k in range(m): # 열로 문자길이만큼 반복
                col.append(data[j + k][i]) # 문자를 하나씩 리스트에 담아준다
            if pali(col): # 문자를 검사해서 True 이면
                ans = ''.join(col) # 리스트 문자열로 변환
                print(f'#{t} {ans}') # 출력
                brk = True # 이중 for문 탈출을 위해 True 설정
                break