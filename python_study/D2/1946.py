# T = int(input())
#
# for i in range(1, T+1):
#     n = int(input())
#     docu = []
#     for i in range(n):
#         a, b = input().split()
#         docu.append([a, b])
#
#     sum_a = ''
#     sum_b = 0
#     for i in docu:
#         a, b = i
#         sum_a += a*int(b)
#         sum_b += int(b)
#
#     limit = sum_b // 10 + 1
#     data = [[] for _ in range(limit)]
#
#     idx = 0
#     for i in sum_a:
#         data[idx].append(i)
#         if len(data[idx]) == 10:
#             idx += 1
#
#     print(f'#{T}')
#     for i in range(limit):
#         print(''.join(data[i]))

T = int(input())

for t in range(1, T+1):
    n = int(input())
    data = ''
    for i in range(n):
        a, b = input().split()
        data += a*int(b)

    lmt = len(data) // 10 + 1

    print(f'#{t}')

    for i in range(lmt-1):
        print(data[i*10:i*10+10])

    print(data[(lmt-1)*10:])