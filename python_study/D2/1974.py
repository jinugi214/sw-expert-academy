T = int(input())

for test_case in range(1, T + 1):
    data = []
    break_value = False
    for i in range(1, 10):
        data.append(list(input().split()))
        
    for i in range(9):
        if len(set(data[i])) != 9:
            print('#'+str(test_case), 0)
            break_value = True
            break
    
        tmp = []
        for j in range(9):
            tmp.append(data[j][i])
        if len(set(tmp)) != 9:
            print('#'+str(test_case), 0)
            break_value = True
            break
    
    if break_value == True:
        continue
            
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            square = []
            for x in range(3):
                for y in range(3):
                    square.append(data[i+x][j+y])
            if len(set(square)) != 9:
                print('#'+str(test_case), 0)
                break_value = True
                break
        if break_value == True:
            break
    if break_value == True:
            continue
                
    print('#'+str(test_case), 1)