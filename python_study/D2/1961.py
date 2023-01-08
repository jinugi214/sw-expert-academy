T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    
    data = []
    
    for i in range(n):
        data.append(list(map(int, input().split())))
        
    print('#'+str(test_case))
    for i in range(n):
        a = ''
        b = ''
        c = ''
        for j in range(n):
            a += str(data[(n-1)-j][i])
            b += str(data[(n-1)-i][(n-1)-j])
            c += str(data[j][(n-1)-i])
        print(a, b, c)