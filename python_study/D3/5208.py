T = int(input())  # 테스트 케이스 입력 후
for tc in range(1, T + 1):  # 순환.
    data = list(map(int, input().split()))  # 버스 정류장당 충전지 입력
    N = data.pop(0)  # 정류장의 갯수 입력
    energy = data[0]  # 첫번째 정류장의 충전지를 가지고 시작
    distance = 0  # 현재 위치는 0으로 시작
    cnt = 0  # 충전지 교환 횟수는 0으로 시작
    while distance + energy < N - 1:  # 현재위치 + 에너지를 가지고 종점으로 갈 수 있으면 반복문종료
        tmp = []  # 일시적 배열.
        for i in range(1, energy + 1):  # 내가 갈 수 있는 정류장을 탐색한다.
            # tmp의 원소당 인덱스는 3개다. 각각 크기비교, 인덱스, distance구할 인덱스
            tmp.append([data[distance + i] + i, distance + i, i])
        # tmp 원소의 첫번째 인덱스로 어디 정류장 갈지 선택. 내림차 순으로 정렬하여 가장 앞에 정렬된 정류장으로 갈 것이다.
        tmp.sort(key=lambda x: x[0], reverse=True)
        # tmp 원소의 두번째 인덱스로 그 정류장의 에너지를 저장
        energy = data[tmp[0][1]]
        # tmp 원소의 세번째 인덱스로 그 정류장일 때 내 위치를 저장
        distance += tmp[0][2]
        cnt += 1  # 카운트

    print(f'#{tc} {cnt}')  # 카운트를 출력