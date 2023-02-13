T = int(input())

for t in range(1, T+1):
    N = int(input())

    pascal = []

    # 맨 앞과 맨 끝은 무조건 1
    # 파스칼 세번째 줄부터 전 리스트참고해서 합을 구해 중간값 넣기

    for i in range(N):
        if i < 2:
            pascal.append([1] * (i+1))
        else:
            tmp = []
            tmp.append(1)
            for j in range(1, i):
                ni = i-1
                nj = j-1
                tmp.append(pascal[ni][nj] + pascal[ni][j])
            tmp.append(1)
            pascal.append(tmp)

    print(f'#{t}')
    for i in range(len(pascal)):
        print(' '.join(map(str, pascal[i])))