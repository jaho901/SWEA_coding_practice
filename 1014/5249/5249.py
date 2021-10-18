import sys
sys.stdin = open('5249.txt')


def find(x): # x의 루트를 찾는 함수
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])   # path compression
        return parent[x]



def union_(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y
    '''
    # union by rank
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1
    '''


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    parent = list(range(V + 1))
    rank = [0 for i in range(V + 1)]

    arr = [list(map(int, input().split())) for _ in range(E)]

    arr.sort(key= lambda x: x[2])   # 가중치 순으로 오른차순 정렬
    # (크루스칼알고리즘: 각 노드에서 다른 노드로 향하는 가중치중 최소값만을 찾아서 연결하면 MST가 된다는 것을 이용)

    ans = 0
    for s, e, w in arr:
        if find(s) == find(e): # 이미 연결되 있으면 넘어가
            continue
        ans += w    # 아니라면 가중치 +, 연결시켜
        union_(s, e)

    print('#{} {}'.format(tc, ans))