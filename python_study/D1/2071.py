t = int(input())

for i in range(t):
    data = list(map(int, input().split()))
    average = round(sum(data) / len(data), 0) 
    print('#'+str(i+1), int(average))