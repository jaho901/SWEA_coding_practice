import sys
sys.stdin = open('5201.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    freight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    freight = sorted(freight, reverse = True)
    truck = sorted(truck, reverse = True)
    result = 0
    visited = [0]*N

    for i in range(M):
        for j in range(N):
            if truck[i] >= freight[j] and not visited[j]:
                result += freight[j]
                visited[j] = 1
                break

    print('#{} {}'.format(tc, result))

