def check_pair(arr):

    rlt = []

    for i in arr:
        if i == '{' or i == '(':
            rlt.append(i)
        elif rlt and i == ')' and rlt[-1] == '(':
            rlt.pop()
        elif rlt and i == '}' and rlt[-1] == '{':
            rlt.pop()
        else:
            return False

    if len(rlt) > 0:
        return False
    else:
        return True


T = int(input())

for t in range(1, T+1):
    data = list(input())
    bracket = []
    for i in data:
        if i == '{' or i == '}' or i == '(' or i == ')':
            bracket.append(i)

    if check_pair(bracket):
        ans = 1
    else:
        ans = 0

    print(f'#{t} {ans}')