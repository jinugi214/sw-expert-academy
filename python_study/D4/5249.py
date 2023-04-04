T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        adj[a][b] = w
        adj[b][a] = w


    ##############################인접행렬 완성
    def prim(start):
        # MST를 만들어가는 과정
        mst = set()  # mst에 포함된 노드를 넣어주는 set
        # 강의 자료에...pi와 key에 해당하는 데이터는
        # weight : 해당 정점을 선택하는 가중치
        weight = [0xffffffff] * (V + 1)
        # 시작정점 잡아주기
        weight[start] = 0
        # 최소 가중치를 가지는 정점을 선택하는 것을 반복
        # >> 모든 정점이 선택될 때 까지 반복
        while len(mst) < V + 1:
            # 최소 가중치 선택하기
            min_v = 0xffffffff
            min_idx = 0  # 의미 없는 0
            # 아직 선택되지 않은 노드이면서...최소 가중치라면 선택
            for i in range(V + 1):
                if i not in mst and weight[i] < min_v:
                    min_v = weight[i]
                    min_idx = i
            # 최소값 구하기가 종료
            mst.add(min_idx)
            # min_idx 번 노드가 선택된거니까....
            # min_idx에서 갈 수 있는 정점까지 가중치가 더 작다면 업데이트
            for i in range(V + 1):
                # weight[i]가 min_idx에서 i번으로 가는 비용보다 더 크다면
                # 아직 i가 mst에 포함되지 않으면서
                # min_idx랑 i랑 연결되어 있는지 확인
                if i not in mst and adj[min_idx][i] \
                        and weight[i] > adj[min_idx][i]:
                    weight[i] = adj[min_idx][i]

        return weight


    result = prim(0)

    print(f'#{t} {sum(result)}')
