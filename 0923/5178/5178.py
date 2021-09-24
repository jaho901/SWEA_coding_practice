import sys
sys.stdin = open('5178.txt')

def binary_sum(data):
    if len(data)%2 == 0:
        pass
    else:
        data[len(data)//2] = data[len(data)-1]

    for i in range(len(data), 1, -1):
        if data[i // 2]:
            pass
        else:
            data[i // 2] = data[i] + data[i - 1]
    return data


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    data = [0 for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        data[x] = y
    print(data)
    binary_sum(data)
    print('#{} {}'.format(tc, data[L]))