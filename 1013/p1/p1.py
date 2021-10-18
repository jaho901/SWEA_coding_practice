import sys
sys.stdin = open('input.txt')

N = 7
data = [[] for _ in range(N+1)]
for _ in range(8):
    u, v = map(int, input().split())
    data[u].append(v)

def dfs(v):
    visited[v]=1
    result.append(v)
    v = stack.pop()

    for i in data[v]:
        if not visited[i]:
            visited[i]=1
            stack.append(i)
            dfs(i)


visited =[0 for _ in range(N+1)]
result = []
stack = [1]
dfs(1)
print(result)