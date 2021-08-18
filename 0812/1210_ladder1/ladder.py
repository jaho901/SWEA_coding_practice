import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T+1):
    tc = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]

    # 가장 끝에부터 시작
    start_pt = 0
    for idx in range(len(ladder)):
        if ladder[N-1][idx] == 2:
            start_pt += idx

    i, j = N-1, start_pt

    while i != 0:
        '''
        if 0 <= j < N:
            if ladder[i][j-1] == 1:
                ladder[i][j] = 0
                j = j-1
            elif ladder[i][j+1] == 1:
                ladder[i][j] = 0
                j = j+1
            else:
                i -= 1
        elif j == 0:
            if ladder[i][j+1] == 1:
                ladder[i][j] = 0
                j = j+1
            else:
                i -= 1
        elif j == N-1:
            if ladder[i][j - 1] == 1:
                ladder[i][j] = 0
                j = j - 1
            else:
                i -= 1
        '''
        if j < 99 and ladder[i][j+1] == 1:
            ladder[i][j] = 0
            j += 1 # 우측이동
        elif 0 < j and ladder[i][j-1] == 1:
            ladder[i][j] = 0
            j -= 1 # 좌측이동
        elif 0 <= j < 100 and ladder[i-1][j] == 1:
            i -= 1 # 위로 올라가

    print('#{0} {1}'.format(tc, j))



