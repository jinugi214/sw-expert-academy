def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = start + (end - start) // 2
        if key == a[middle]: # 검색 성공
            return True
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
