import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    ans = 10*N

    def recur(cur = 0, total = 0):
        global ans
        
        # DFS
        if cur == N:
            ans = min(ans, total)
            return
        
        # 빽트래킹
        if total > ans:
            return

        # 순열
        for i in range(N):
            if visited[i]:
                continue

            visited[i] = True
            recur(cur + 1, total + data[cur][i])
            visited[i] = False

    recur(0, 0)

    print('#{} {}'.format(tc, ans))