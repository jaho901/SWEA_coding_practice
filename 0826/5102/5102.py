import sys

sys.stdin = open('input.txt')

def bfs(sp, V):
    # global visited
    q = [0] * V
    visited = [0] * (V + 1)
    front = -1
    rear = -1
    rear += 1
    q[rear] = sp
    visited[sp] = 1

    while front != rear:
        front += 1
        t = q[front]
        for i in range(1, V+1):
            if adj[t][i] == 1 and not visited[i]:
                rear += 1
                q[rear] = i
                visited[i] = visited[t] + 1



T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        adj[s][e] += 1
        adj[e][s] += 1
    sp, ep = map(int, input().split())
    visited = [0] * (V + 1)

    bfs(sp, V)
    if visited[ep] == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, visited[ep] - 1))
