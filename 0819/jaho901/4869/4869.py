import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = [1]

    for i in range(1, N//10):
        if i % 2 == 1:
            num = result[i-1] * 2 + 1
            result.append(num)

        elif i % 2 == 0:
            num = result[i-1] * 2 - 1
            result.append(num)

    print('#{} {}'.format(tc, result[-1]))


'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tile = {}
    for i in range(10, N+1, 10):
        tile[i] = 0
    # print(tile)
    '''
    {10: 0, 20: 0, 30: 0}
    {10: 0, 20: 0, 30: 0, 40: 0, 50: 0}
    {10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
    '''
    tile[10] = 1 #가로 10 1개
    tile[20] = 3 #가로 20 2개 세로로 정열한 것은 가로 10에 포함
    print(tile)
    for i in range(30, N+1, 10):
        tile[i] = tile[i-10] + tile[i-20]*2

    print('#{} {}'.format(tc,tile[N]))
'''