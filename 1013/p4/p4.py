import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

N, M = map(int, input().split())
K = int(input())
data = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    data[u].append([w, v])
INF = 10000000

heap = []
visited = [INF] * (N + 1)

def dijkstra(K):
    visited[K] = 0
    heappush(heap, [0, K])

    while heap:
        w, v = heappop(heap)

        for next_w, next_v in data[v]:
            nw = w + next_w
            if nw < visited[next_v]:
                visited[next_v] = nw
                heappush(heap, [nw, next_v])

dijkstra(K)
for i in range(len(visited)):
    if visited[i] == INF:
        visited[i] = 0
print(visited)