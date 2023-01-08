T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split()) 
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    
    result = 0
    
    if n >= m:
        long_list = n_list
        short_list = m_list
    else:
        long_list = m_list
        short_list = n_list   
    
    
        
    move = abs(n-m)+1
    for i in range(move): # 0,1,2
        tmp = 0
        for j in range(len(short_list)): # 0,1,2
            tmp += short_list[j] * long_list[j+i]
        if tmp > result:
            result = tmp    
    
    print('#'+str(test_case), result)