T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*(N-M+1) for _ in range(N-M+1)]

    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(M):
                for l in range(M):
                    result[i][j] += arr[i+k][j+l]

    maximum = 0
    for x in result:
        for y in x:
            if maximum < y:
                maximum = y
    print('#{} {}'.format(tc, maximum))