import sys
sys.stdin = open('5251.txt')
from heapq import heappop, heappush

def dijkstra(K):
    visited[K] = 0
    heappush(heap, [0, K])

    while heap:
        w, e = heappop(heap)
        for next_w, next_e in node[e]:
            nw = next_w + w
            if nw < visited[next_e]:
                visited[next_e] = nw
                heappush(heap, [nw, next_e])


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    node = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        node[s].append([w, e])

    INF = 1000000000
    heap = []
    visited = [INF] * (N+1)

    dijkstra(0)
    print('#{} {}'.format(tc, visited[N]))