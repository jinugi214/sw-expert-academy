def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
            a[i], a[min] = a[min], a[i]

    return a


print(selectionSort([3, 5, 1, 2, 4, 0]))
