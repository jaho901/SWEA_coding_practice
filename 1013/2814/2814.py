import sys
sys.stdin=open('2814.txt')


def dfs(start, ans):
    global result
    visited[start]=1
    if ans > result:
        result = ans

    for i in data[start]:
        if not visited[i]:
            visited[i] = 1
            dfs(i,ans+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    data = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int,input().split())
        data[x].append(y)
        data[y].append(x)

    result = 0

    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i,1)

    print('#{} {}'.format(tc, result))