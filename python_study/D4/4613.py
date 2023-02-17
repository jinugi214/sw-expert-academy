T = int(input())

# 해당 행을 color로 전부 바꿀 때 라인별 필요한 색칠 횟수
def color_line(flag, color):
    rlt = []
    for i in range(N):
        cnt = 0
        for j in range(M):
            if flag[i][j] != color:
                cnt += 1
        rlt.append(cnt)
    return rlt

for t in range(1, T+1):
    N, M = map(int, input().split())

    flag = [list(input()) for _ in range(N)]

    # 맨윗줄 무조건 전부 W
    # 중간에 전부 B가 한줄은 들어가야함
    # 맨아랫줄 무조건 전부 R

    # 완전탐색으로 모든 라인을 색깔별로 변환식 필요 횟수를 리스트로 저장
    white_lst = color_line(flag, 'W')
    blue_lst = color_line(flag, 'B')
    red_lst = color_line(flag, 'R')

    min_c = 1e9
    for i in range(N-2): # 화이트의 경우
        for j in range(i+1, N-1): # 블루의 경우 (화이트, 블루 정해지면 레드는 자동으로 정해짐)
            cnt_list = white_lst[:i+1] + blue_lst[i+1:j+1]+red_lst[j+1:N]
            cnt = sum(cnt_list)
            if cnt < min_c:
                min_c = cnt

    print(f'#{t} {min_c}')

