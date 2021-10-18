import sys
sys.stdin = open('1952.txt')


def dfs(cur, total):
    global result
    if cur >= 12:
        result = min(result, total)
        return

    if result < total:
        return

    dfs(cur + 1, total + money[0] * plan[cur])
    dfs(cur + 1, total + money[1])
    dfs(cur + 3, total + money[2])


T = int(sys.stdin.readline())
for tc in range(1 ,T+1):
    money = list(map(int, sys.stdin.readline().split()))
    plan = list(map(int, sys.stdin.readline().split()))

    result = money[3]
    dfs(0, 0)
    print('#{} {}'.format(tc, result))
