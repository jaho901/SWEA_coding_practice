import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    matrix = [[0] * 10 for _ in range(10)]

    for case in arr:
        i1, i2 = case[0], case[2]
        j1, j2 = case[1], case[3]
        color = case[4]
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                if matrix[i][j] == color:
                    pass
                else:
                    matrix[i][j] += color

    result = 0
    for i in matrix:
        for j in i:
            if j == 3:
                result += 1

    print('#{0} {1}'.format(tc, result))




