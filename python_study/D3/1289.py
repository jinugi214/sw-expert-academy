t = int(input())

for test_case in range(1, t+1):

    cnt = 0

    text = input()

    start = ['0']*len(text)

    for i in range(len(text)):
        if start[i] != text[i]:
            start[i:] = text[i] * len(start[i:])
            cnt += 1

    print(f'#{test_case} {cnt}')