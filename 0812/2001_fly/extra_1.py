import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    result = 0


    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            fly = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    fly += matrix[k][l]
            result = max(result, fly)


    print('#{0} {1}'.format(tc, result))


