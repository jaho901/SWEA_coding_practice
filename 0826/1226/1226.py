import sys
sys.stdin = open('input.txt')

def bfs(sx, sy):
    global ans
    queue = [[sx, sy]]
    visited[sx][sy] = 1
    result = False

    while queue:
        now = queue.pop(0)
        sx = now[0]
        sy = now[1]

        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if data[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                if data[nx][ny] == 3:
                    ans = 1
                    result = True
                    break
        if result:
            break


T = 10
for _ in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    ans = 0
    visited = [[0] * 16 for _ in range(16)]
    sx, sy = 0, 0
    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                sx = i
                sy = j

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ans = 0

    bfs(sx, sy)
    print('#{} {}'.format(tc, ans))