import sys
sys.stdin = open('5247.txt')
from collections import deque


def bfs(N, M):
    global result

    queue = deque()
    queue.append(N)
    visited[N] = 0

    while queue:
        x = queue.popleft()

        if x == M:
            result = visited[M]
            break

        for nx in (x+1, x-1, x*2, x-10):
            if 0 <= nx <= maximum and not visited[nx]:
                visited[nx] = visited[x]+1
                queue.append(nx)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    maximum = 1000000
    visited = [0] * (maximum + 1)
    result = 0
    bfs(N, M)
    print('#{} {}'.format(tc, result))
