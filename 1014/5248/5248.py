import sys
sys.stdin = open('5248.txt')
from collections import deque
import heapq

# def bfs(k, num):
#     queue = deque()
#     queue.append(k)
#     visited[k] = num
#
#     while queue:
#         x = queue.popleft()
#
#         for nx in group[x]:
#             if not visited[nx]:
#                 visited[nx] = num
#                 queue.append(nx)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     data = list(map(int, input().split()))
#     group = [[]for _ in range(N+1)]
#     for i in range(0, 2*M, 2):
#         group[data[i]].append(data[i+1])
#         group[data[i+1]].append(data[i])
#
#     visited=[0]*(N+1)
#     num = 1
#
#     for i in range(1, N+1):
#         if not visited[i]:
#             bfs(i, num)
#             num += 1
#
#     print('#{} {}'.format(tc, num-1))

heap = []
heapq.heappush(heap, 5)
print(heap)
heapq.heappop(heap)
print(heap)
