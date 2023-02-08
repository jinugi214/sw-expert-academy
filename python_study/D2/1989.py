# title : 초심자의 회문 검사

T = int(input())

for t in range(1, T+1):
    text = input()
    ans = 0
    check = text[::-1]
    if text == check:
        ans = 1

    print(f'#{t} {ans}')