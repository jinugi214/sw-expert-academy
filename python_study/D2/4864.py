# title: 문자열 비교
# 브루트 포스

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    ans = 0
    limit = len(str2) - len(str1) + 1
    for i in range(limit):
       if str1 == str2[i:len(str1) + i]:
           ans = 1
           break

    print(f'#{t} {ans}')