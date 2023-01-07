from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    test_number = input()
    data = list(map(int, input().split()))

    cnt = Counter(data)

    print('#'+test_number, cnt.most_common(1)[0][0])