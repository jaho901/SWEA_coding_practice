import sys
sys.stdin = open('5174.txt')

def dfs(x):
    global cnt
    if node[x]:
        for i in node[x]:
            cnt += 1
            dfs(i)
    else:
        return

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = [[] for _ in range(E+2)]
    data = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        node[data[i]].append(data[i+1])
    # print(node)
    cnt = 1
    dfs(N)
    print('#{} {}'.format(tc, cnt))
