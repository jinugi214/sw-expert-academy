# title : 숫자 배열 회전

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a = [[0] * N for _ in range(N)] # 90도
    b = [[0] * N for _ in range(N)] # 180도
    c = [[0] * N for _ in range(N)] # 270도

    # 회전각도에 따른 위치 값을 저장
    for i in range(N):
        for j in range(N):
            a[i][j] = arr[N-1-j][i]
            b[i][j] = arr[N-1-i][N-1-j]
            c[i][j] = arr[j][N-1-i]

    print(f'#{test_case}')
    for dg90, dg180, dg270 in zip(a, b, c):
        print(f'{"".join(dg90)} {"".join(dg180)} {"".join(dg270)}')