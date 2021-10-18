import sys
sys.stdin = open('1865.txt')

def dfs(cur, total):
    global result

    if cur == N:
        result = max(result, total)
        return

    # 백트래킹 조건 완료
    if result >= total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(cur+1, total*prob[i][cur]/100)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # result값을 음수로 큰수로 지정해야지 다른 케이스 통과한다!!
    result = -1000000
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, result*100))