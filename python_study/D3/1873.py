T = int(input())

for t in range(1, T+1):

    h, w = map(int, input().split())

    game_map = []
    for _ in range(h):
        game_map.append(list(input()))

    tank = ['^', 'v', '<', '>']

    for i in range(h):
        for j in range(w):
            if game_map[i][j] in tank:
                x, y = i, j

    n = int(input())

    cmd_line = list(input())

    def check(x, y):
        if 0 <= x < h and 0 <= y < w:
            return True
        else:
            return False

    for cmd in cmd_line:
        if cmd == 'U':
            if check(x-1, y) and game_map[x-1][y] == '.':
                game_map[x][y] = '.'
                x, y = x-1, y
                game_map[x][y] = '^'
            else:
                game_map[x][y] = '^'
        elif cmd == 'D':
            if check(x+1, y) and game_map[x+1][y] == '.':
                game_map[x][y] = '.'
                x, y = x+1, y
                game_map[x][y] = 'v'
            else:
                game_map[x][y] = 'v'
        elif cmd == 'L':
            if check(x, y-1) and game_map[x][y-1] == '.':
                game_map[x][y] = '.'
                x, y = x, y-1
                game_map[x][y] = '<'
            else:
                game_map[x][y] = '<'
        elif cmd == 'R':
            if check(x, y+1) and game_map[x][y+1] == '.':
                game_map[x][y] = '.'
                x, y = x, y+1
                game_map[x][y] = '>'
            else:
                game_map[x][y] = '>'
        elif cmd == 'S':
            if game_map[x][y] == '^':
                for i in range(x-1, -1, -1):
                    if game_map[i][y] == '#':
                        break
                    if game_map[i][y] == '*':
                        game_map[i][y] = '.'
                        break
            elif game_map[x][y] == 'v':
                for i in range(x+1, h):
                    if game_map[i][y] == '#':
                        break
                    if game_map[i][y] == '*':
                        game_map[i][y] = '.'
                        break
            elif game_map[x][y] == '<':
                for i in range(y-1, -1, -1):
                    if game_map[x][i] == '#':
                        break
                    if game_map[x][i] == '*':
                        game_map[x][i] = '.'
                        break
            elif game_map[x][y] == '>':
                for i in range(y+1, w):
                    if game_map[x][i] == '#':
                        break
                    if game_map[x][i] == '*':
                        game_map[x][i] = '.'
                        break

    print(f'#{t}', end=' ')
    for i in range(h):
        print(''.join(game_map[i]))
