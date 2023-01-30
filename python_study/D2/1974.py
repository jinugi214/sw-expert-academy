T = int(input())

def square(x, y):
    square_list = []

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            square_list.append(puzzle[i][j])
    return square_list


def check(puzzle):
    if len(set(puzzle)) != 9:
        return False

    if sum(puzzle) != 45:
        return False

    for num in puzzle:
        if num > 9:
            return False

    return True


for t in range(1, T+1):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))

    ans = 1

    for i in range(9):
        if not check(puzzle[i][:9]):
            ans = 0
            break

    if ans == 0:
        print(f'#{t} {ans}')
        continue

    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(puzzle[j][i])

        if not check(tmp):
            ans = 0
            break

    if ans == 0:
        print(f'#{t} {ans}')
        continue

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check(square(i, j)):
                ans = 0
                break
        if ans == 0:
            break

    print(f'#{t} {ans}')
