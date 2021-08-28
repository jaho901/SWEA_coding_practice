import sys

sys.stdin = open('input.txt')

def bfs(sx, sy, N):
    # global visited
    visited = [[0] * N for _ in range(N)]
    q = [0]*N*N
    front = -1
    rear = -1

    rear += 1
    q[rear] = [sx, sy]
    visited[sx][sy] = 1

    while front != rear:
        front += 1
        tx, ty = q[front][0], q[front][1]

        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] == 0 and visited[nx][ny] == 0:
                    rear += 1
                    q[rear] = [nx, ny]
                    visited[nx][ny] = visited[tx][ty] + 1
                elif data[nx][ny] == 3:
                    result = visited[tx][ty]
                    return result - 1



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sx, sy = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    k = 0
    for x in range(len(data)):
        for y in range(len(data)):
            if data[x][y] == 2:
                sx = x
                sy = y
    if bfs(sx, sy, N):
        print('#{} {}'.format(tc, bfs(sx, sy, N)))
    else:
        print('#{} {}'.format(tc, 0))
