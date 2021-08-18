import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):

    n = input()

    matrix = [list(map(int, input().split())) for _ in range(100)]
    summation = []

    # 행과 열의 합
    for i in range(len(matrix)):
        width_sum = 0
        height_sum = 0
        diag = 0
        diag_rev = 0
        for j in range(len(matrix)):
            # 행은 i,1 + i,2 + --- + i,100
            width_sum += matrix[i][j]

            # 열은 1,j + 2,j + --- + 100,j
            height_sum += matrix[j][i]

        # 정 대각선은 i,i
        diag += matrix[i][i]

        # 역 대각선은 0,99 + 1,98 + 2,97, + --- + 97,2 + 98,1 + 99,0
        diag_rev += matrix[i][99-i]

        summation.append(width_sum)
        summation.append(height_sum)
        summation.append(diag)
        summation.append(diag_rev)

    print('#{0} {1}'.format(tc, max(summation)))


    '''
    # 교수님 풀이
    
    data = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합 (0,0) (0,1) ...
    result_1 = 0
    # 열의 합 (0,0) (1,0) ...
    result_2 = 0
    # 대각선의 합 1 (0,0) (1,1) ...
    result_3 = 0
    # 대각선의 합 2 (99-0, 99-0) (99-1, 99-1) ...(0, 0)
    result_4 = 0

    for i in range(100):
        result_3 += data[i][i]
        result_4 += data[99-i][99-i]
        tmp_1 = 0
        tmp_2 = 0
        for j in range(100):
            tmp_1 += data[i][j]
            tmp_2 += data[j][i]
        if tmp_1 > result_1:
            result_1 = tmp_1
        if tmp_2 > result_2:
            result_2 = tmp_2

    print('#{} {}'.format(tc, max(result_1, result_2, result_3, result_4)))
    
    '''








