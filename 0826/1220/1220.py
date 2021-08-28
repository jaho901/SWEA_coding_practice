import sys
sys.stdin = open('input.txt')


def find(a):
    b = []
    for i in range(N):
        if a[i] !=  0:
            b.append(a[i])
    return b

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    for ie in zip(*data):
        arr.append(list(ie))

    total = 0
    for row in arr:
        sub = find(row)
        n = 0
        while sub:
            if len(sub) == 1:
                sub.pop(0)
                break
            if sub[0] == 1 and sub[1] == 2:
                total += 1
                sub.pop(0)
                sub.pop(0)
            elif sub[0] == 2 and sub[1] == 1:
                total += 1
                sub.pop(0)
                sub.pop(0)
            else:
                sub.pop(0)
    print(total)



