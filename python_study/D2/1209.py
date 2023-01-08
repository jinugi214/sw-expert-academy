test_case = 10
num = 0
while num < test_case:
    test_number = input()
    
    data = []
    for i in range(100):
        data.append(list(map(int, input().split())))
    
    result_list = [0] * 100
    
    for i in range(100):
        result_list[i] = sum(data[i])
    
    for i in range(100):
        column_value = 0
        for j in range(100):
            column_value += data[j][i]
        if column_value > result_list[i]:
            result_list[i] = column_value
    
    print('#'+test_number, max(result_list))
    num += 1