import sys

sys.stdin = open('5202.txt')

def dfs(cur):
    global result, ans

    for i in range(cur+1, N):
        if data[cur][1] <= data[i][0] and not visited[i]:
            visited[i] = 1
            result += 1
            dfs(i)
            ans = max(ans, result)
            visited[i] = 0
            result -= 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = []
    for _ in range(N):
        s, e = map(int, input().split())
        data.append([s, e])
    data = sorted(data, key=lambda x:x[0])
    visited = [0]*N
    # print(data)
    result = 1
    ans = 0

    for i in range(N):
        dfs(i)
    print('#{} {}'.format(tc, ans))
