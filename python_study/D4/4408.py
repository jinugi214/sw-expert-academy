# title: 자기 방으로 돌아가기

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = [0] * 201
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start

        for i in range((start + 1) // 2, (end + 1) // 2 + 1):
            cnt[i] += 1
    print(f'#{test_case} {max(cnt)}')