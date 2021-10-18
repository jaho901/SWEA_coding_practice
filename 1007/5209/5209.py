import sys
sys.stdin = open('5209.txt')

def dfs(cur, total):
    global result
    if cur == N:
        result = min(result, total)
        return

    # 백트래킹을 의미하는 부분
    if result < total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(cur+1, total + arr[i][cur])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10000000
    visited = [0]*N
    dfs(0, 0)
    print('#{} {}'.format(tc, result))
