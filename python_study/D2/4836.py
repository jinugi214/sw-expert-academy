T = int(input())

def coloring(x1, y1, x2, y2, color):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if color == 1:
                if graph[x][y] == 0:
                    graph[x][y] = 1
                elif graph[x][y] == 1:
                    continue
                elif graph[x][y] == 2:
                    graph[x][y] = 3
            elif color == 2:
                if graph[x][y] == 0:
                    graph[x][y] = 2
                elif graph[x][y] == 1:
                    graph[x][y] = 3
                elif graph[x][y] == 2:
                    continue


for t in range(1, T + 1):
    graph = [[0] * 10 for _ in range(10)]
    n = int(input())
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        coloring(x1, y1, x2, y2, color)

    cnt = 0

    for i in range(10):
        for j in range(10):
            if graph[i][j] == 3:
                cnt += 1

    print(f'#{t} {cnt}')
