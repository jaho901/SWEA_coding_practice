import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    c = list(map(int, input().split()))

    pizza = []
    for i in range(1, M+1):
        pizza.append([i, c[i-1]])

    data = pizza[:N]


    while True:
        data[0][1] = data[0][1]//2
        if data[0][1] == 0 and N+1 <= M:
            data[0] = pizza[N]
            N += 1
        a = data.pop(0)
        data.append(a)
        total = 0
        for i in data:
            total += i[1]
        if total == 1:
            break


    idx = 0
    for i in range(len(data)):
        if data[i][1] == 1:
            idx = i
        else:
            pass
    print('#{} {}'.format(tc, data[idx][0]))


