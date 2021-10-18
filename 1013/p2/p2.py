import sys
sys.stdin = open('input.txt')
from collections import deque

N = 7
data = [[] for _ in range(N+1)]
for _ in range(8):
    u, v = map(int, input().split())
    data[u].append(v)


def bfs():
    Q = deque()
    Q.append(1)
    while Q:
        v = Q.popleft()
        result.append(v)
        for i in data[v]:
            if not visit[i]:
                visit[i] = 1
                Q.append(i)


visit = [ 0 for _ in range(N+1)]
result =[]
bfs()
print(result)
