T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(1, N):
        for j in range(1, N):
            tmp = data[i][j]
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                for dif in range(1, M):
                    nx, ny = i + dx*dif, j + dy*dif
                    if 0<= nx < N and 0 <= ny < N:
                        tmp += data[nx][ny]
            ans = max(ans, tmp)
            
            tmp = data[i][j]
            for dx, dy in ((-1,-1),(-1,1),(1,-1),(1,1)):
                for dif in range(1, M):
                    nx, ny = i + dx*dif, j+dy*dif
                    if 0<=nx<N and 0<=ny<N:
                        tmp += data[nx][ny]
            ans = max(ans, tmp)
    print(f'#{t} {ans}')