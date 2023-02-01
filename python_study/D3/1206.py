for t in range(1, 11):
    n = int(input())

    bd = list(map(int, input().split()))

    view = 0

    for i in range(2, n-2):
        left1 = bd[i] - bd[i-2] # 왼쪽 두칸과 비교
        left2 = bd[i] - bd[i-1]
        right1 = bd[i] - bd[i+1]
        right2 = bd[i] - bd[i+2] # 오른쪽 두칸과 비교

        if left1 < 0 or left2 < 0 or right1 < 0 or right2 < 0:
            continue
        else: # 왼쪽두칸부터 오른쪽 두칸까지 중에 가장 높은 빌딩 찾기
            around = [left1, left2, right1, right2]
            min_bd = left1
            for x in around:
                if min_bd > x:
                    min_bd = x
            view += min_bd

    print(f'#{t} {view}')
