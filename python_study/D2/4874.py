# title: Forth

T = int(input())

def cal_result(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b

for t in range(1, T + 1):
    data = list(input().split())
    stack = []
    rlt = 0

    for i in data:
        if i in ['+', '-', '*', '/']:
            if len(stack) > 1:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(cal_result(b, a, i))
            else:
                rlt = 'error'
                break
        elif i == '.':
            if len(stack) == 1:
                rlt = stack[0]
                break
            else:
                rlt = 'error'
                break
        else:
            stack.append(i)

    print(f'#{t} {rlt}')