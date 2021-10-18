import sys
sys.stdin = open('5250.txt')
from collections import deque
from heapq import heappush, heappop

'''
1 X N 인 리스트를 사용한 bfs가 아닌

(0, 0)에서 (N-1, N-1)로 이동하는 최소거리를
구하는 다익스트라 알고리즘이라서 힙큐 사용할 수 있고, 

또한, N X N 인 array를 사용한 bfs이기 때문에
일반적인 리스트가 아닌 더블엔디드큐를 사용해주었다.

두 방법을 사용하여 시간복잡도를 줄여줄 수 있다.

'''
# bfs 함수 생성
def bfs(x, y):
    # 1. 큐 생성
    queue = deque()
    # 2. 큐에 초기값 삽입 & 초기값 위치 방문처리
    queue.append([x, y])
    visited[x][y] = 0
    
    # 3. 큐가 비어있을 때 까지 반복문 돌리기
    while queue:
        x, y = queue.popleft()
        # 4. for문과 조건문을 통해 현재 위치에서 이동가능한 다음위치로 이동
        for k in range(4):
            # 이동가능한 다음위치의 인덱스 nx, ny 지정
            nx ,ny = x + dx[k], y + dy[k]
            # 이동가능한 조건문
            if 0 <= nx < N and 0 <= ny < N:
                diff = 0
                # 다음위치가 높아졌다면 높이 차이를 diff에 저장
                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]
                # 다음 위치 값이 최솟값이면 최솟값에 높이 차이를 더해준 값을 지정
                if visited[nx][ny] > visited[x][y] + diff + 1:
                    visited[nx][ny] = visited[x][y] + diff + 1
                    # 이동 가능한 위치를 큐에 삽입
                    queue.append([nx, ny])


# dijkstra 함수 생성
def dijkstra(x, y):
    # 1. 큐 생성
    heap = []
    # 2. 큐에 초기값 삽입 & 초기값 위치 방문처리
    heappush(heap, [x, y])
    visited[x][y] = 0

    # 3. 큐가 비어있을 때 까지 반복문 돌리기
    while heap:
        x, y = heappop(heap)
        # 4. for문과 조건문을 통해 현재 위치에서 이동가능한 다음위치로 이동
        for k in range(4):
            nx ,ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                diff = 0
                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]
                if visited[nx][ny] > visited[x][y] + diff + 1:
                    visited[nx][ny] = visited[x][y] + diff + 1
                    heappush(heap, [nx, ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited에 담을 가장 큰 값을 INF로 저장
    INF = 1000000000
    visited = [[INF]*N for _ in range(N)]
    # 다음 위치로 이동할 방향벡터 설정
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # bfs(0, 0)
    dijkstra(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))
