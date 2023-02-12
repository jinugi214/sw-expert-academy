# 처음부터 끝까지 전부 검색
def sequentialSearch(a, n, key): # (정렬 안되어있는 경우) 순차 검색
    i = 0
    while i < n and a[i] != key:
        i = i + 1

    if i < n: return i
    else: return -1

print(sequentialSearch([5, 4, 3, 2, 0 ,1], 6, 3))

# 검색 실패시 검색 도중 반환
def sequentialSearch(a, n, key): # (정렬되어있는 경우) 순차 검색
    i = 0
    while i < n and a[i] < key:
        i = i + 1

    if i < n and a[i] == key : return i #
    else: return -1

