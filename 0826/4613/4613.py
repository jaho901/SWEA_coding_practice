import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF-8')

def recur(cur = 0, total = 0, start = 0):
    global ans
    if cur == N:
        ans = min(ans, total)
        return

    if cur == 0:
        recur(cur+1, total+data[cur][0], start)
    elif cur == 1:
        for i in range(start, 2):
            recur(cur+1, total+data[cur][i], start+i)
    elif cur == N-1:
        start = 2
        recur(cur+1, total+data[cur][2], start)
    elif cur == N-2:
        if start == 0:
            start = 1
            recur(cur+1, total+data[cur][start], start)
        else:
            for i in range(start, 3):
                start = i
                recur(cur+1, total+data[cur][start], start)
    else:
        if start <= 1:
            for k in range(start, start+2):
                recur(cur + 1, total+data[cur][k], k)
        else:
            recur(cur + 1, total+data[cur][2], 2)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = [list(input()) for _ in range(N)]
    data = []
    for i in range(len(a)):
        w = 0
        b = 0
        r = 0
        for j in range(len(a[0])):
            if a[i][j] == 'W':
                w += 1
            elif a[i][j] == 'B':
                b += 1
            else:
                r += 1
        data.append([M-w, M-b, M-r])
    ans = 50*50
    recur(0, 0, 0)
    print('#{} {}'.format(tc, ans))






