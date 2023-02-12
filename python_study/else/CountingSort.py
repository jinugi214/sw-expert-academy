def Counting_Sort(A, B, k):
    # A = [] 입력 배열
    # B = [] 정렬된 배열
    # C = [] 카운트 배열

    C = [0] * (k+1)

    for i in range(0, len(A)):
        C[A[i]] += 1 # 각 개수 세기

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    return B

A = [0, 1, 3, 5, 4, 2]
B = [0] * len(A)
print(Counting_Sort(A, B, 6))