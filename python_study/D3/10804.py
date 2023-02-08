# title: 문자열의 거울상

T = int(input())

for t in range(1, T+1):

    ans = []
    text = list(input())
    for i in text:
        if i == 'q':
            ans.append('p')
        elif i == 'p':
            ans.append('q')
        elif i == 'b':
            ans.append('d')
        elif i == 'd':
            ans.append('b')
    # q -> p
    # p -> q
    # b -> d
    # d -> b

    ans = ''.join(ans[::-1])

    print(f'#{t} {ans}')