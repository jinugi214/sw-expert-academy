# 진기의 최고급 붕어빵

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명이 붕어빵 살 수 있다.
    # M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.

    data = list(map(int, input().split()))
    data.sort()
    # 각 정수는 각 사람이 언제 도착하는지를 초 단위
    
    # 모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면
    # “Possible”을, 아니라면 “Impossible”을 출력
    ans = 'Possible'

    people = 0
    for p in data:
        people += 1
        if people > (p // M) * K:
            ans = 'Impossible'
            break

    print(f'#{t} {ans}')