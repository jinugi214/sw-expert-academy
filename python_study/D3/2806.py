T = int(input())

def check(x):
    for i in range(x):
        # 그전에 퀸이 같은 열에 있거나 또는 대각선에 있으면
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def queens(x):
    global ans
    if x == N: # N개 퀸 다 놓았을 때
        ans += 1
        return

    else:
        for i in range(N):
            row[x] = i # 해당 행에 퀸을 놓아보자
            if check(x): # 놓을 수 있으면
                queens(x + 1) # 다음 행에도 퀸을 놓으러 가자

for t in range(1, T+1):
    N = int(input())
    row = [0] * N
    ans = 0

    # 같은 행, 열, 또는 대각선에 말이 2개 있으면 안된다.
    queens(0)

    print(f'#{t} {ans}')
