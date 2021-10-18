import sys
sys.stdin = open('5208.txt')

def dfs(cur, cnt):
    global result

    if cur >= N-1:
        result = min(result, cnt)
        return

    # 백트래킹을 의미하는 부분
    if result <= cnt:
        return

    for i in range(cur+battery[cur], cur, -1):
        cnt += 1
        dfs(i, cnt)
        cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    battery = list(map(int, input().split()))
    N = battery[0]
    battery = battery[1:]

    result = 10000000
    dfs(0, 0)
    print('#{} {}'.format(tc, result-1))


