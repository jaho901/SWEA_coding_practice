import sys
sys.stdin = open('5656.txt')

def check(i, j):
    global cnt
    num = arr[i][j]
    arr[i][j] = 0
    if num == 1:
        cnt += 1
    else:
        for k in range(3):
            N = num
            x, y = i, j
            while N > 1:
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == 1:
                        pass
                    elif arr[nx][ny] == 0:
                        x, y = nx, ny
                        N -= 1
                        continue

                    elif arr[nx][ny] > 1:
                        check(nx, ny)
                    arr[nx][ny] = 0
                    x, y = nx, ny
                    cnt += 1
                    N -= 1
                else:
                    break

def fall():


T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, W, H = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    check(1, 2)
    print(cnt)
    check(2, 2)
    print(cnt)
    for i in arr:
        print(*i)
