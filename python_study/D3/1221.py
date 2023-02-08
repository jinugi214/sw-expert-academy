# title : GNS
'''
# sort를 사용한 방식
T = int(input())

sort_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR": 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

for _ in range(T):
    t, n = input().split()
    data = list(input().split())
    data.sort(key=lambda x : sort_dict[x])

    print(t)
    print(' '.join(data))
'''

# sort를 사용하지 않은 삽입정렬 방식
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if sort_dict[arr[i - 1]] > sort_dict[arr[i]]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

T = int(input())

sort_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR": 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

for _ in range(T):
    t, n = input().split()
    data = list(input().split())
    insertion_sort(data)

    print(t)
    print(' '.join(data))