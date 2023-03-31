# 정식이의 은행업무

from copy import deepcopy

T = int(input())


def check(two, three):
    for i in range(len(two)):
        for j in range(2):  # 2진수
            if i == 0 and j == 0:
                continue
            else:
                two_tmp = deepcopy(two)
                two_tmp[i] = str(j)
                if two_tmp == two:
                    continue
                two_val = ''.join(two_tmp)
                two_ten = int(two_val, 2)
                for k in range(len(three)):
                    for l in range(3):  # 3진수
                        if k == 0 and l == 0:
                            continue
                        else:
                            three_tmp = deepcopy(three)
                            three_tmp[k] = str(l)
                            if three_tmp == three:
                                continue
                            three_val = ''.join(three_tmp)
                            three_ten = int(three_val, 3)
                            if two_ten == three_ten:
                                return two_ten


for t in range(1, T + 1):
    two = list(input())
    three = list(input())

    # 2진수와 3진수를 바꿀 때마다 같은 지 확인
    # 첫번째 자리는 0 안됨

    print(f'#{t} {check(two, three)}')
