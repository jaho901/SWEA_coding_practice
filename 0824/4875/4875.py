import sys
sys.stdin = open('input.txt')
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    def recur(x, y):
        global result
        if not 0 <= x < N or not 0 <= y < N:
            return

        value = data[x][y]
        if value == 2:
            result = 1
            return

        if value == 0 or value == 3:
            data[x][y] = 1
            return (recur(x-1, y) or recur(x+1, y) or recur(x, y-1) or recur(x, y+1))

        else:
            return

    # 3 <-> 2 가 가능한 경우 살펴보기
    # 데이터에 2와 3이 있는지의 여부 확인하기
    ck_2 = 0
    ck_3 = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                ck_2 = 1
            if data[i][j] == 3:
                x = i
                y = j
                ck_3 = 1
        if ck_2 and ck_3:
            break

    result = 0

    # 2와 3이 있으면 재귀를 돌리고 아니면 error반환
    if ck_2 == 1 and ck_3 == 1:
        recur(x, y)
        print('#{} {}'.format(tc, result))

    else:
        print('#{} {}'.format(tc, 'error'))
'''

    
    # 관이형 코드 (방문목록과 방향벡터 사용 재귀)

def dfs(sy, sx):
    global result  # 출력을 위한 최종값

    if Maze[sy][sx] == 3:  # 만약 도착점이 2라면 도착했다는 뜻이므로 1을 result에 넣고 함수 종료
        result = 1
        return
    visited.append((sy, sx))  # 그 지점을 방문했다는 표시를 남겨주기 위해 visited에 좌표 저장.
    # visited[sy][sx] = 1

    for i in range(4):  # 4방위로 갈 수 있는지 체크하기 위한 for문
        ny = sy + dy[i]
        nx = sx + dx[i]
        # 0보다 크고 N보다 좌표가 작아야된다(벽을 만나면 실행x), 0이거나 2여야 갈 수 있다, 다음 좌표값이 방문을 안했다.
        # if 0 <= ny < n and 0 <= nx < n and Maze[ny][nx] != 1 and visited[ny][nx] == 0:
        if 0 <= ny < n and 0 <= nx < n and Maze[ny][nx] != 1 and (ny, nx) not in visited:
            dfs(ny, nx)


TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    Maze = [list(map(int, input())) for _ in range(n)]
    visited = []  # 방문한 흔적을 남기기 위한 빈 리스트
    # visited = [[0]*n for _ in range(n)]
    # 시작 지점을 탐색해서 시작 좌표를 dfs함수에 넣어주기 위해 좌표를 찾는 반복문
    for y in range(n):
        for x in range(n):
            if Maze[y][x] == 2:
                sy, sx = y, x
    # 우, 하, 좌, 상 방향벡터
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

    result = 0  # 최종 결과값
    dfs(sy, sx)
    print('#{} {}'.format(tc, result))














