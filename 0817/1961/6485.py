def solution(data):
    arr = []
    for re in zip(*data):
        arr.append(''.join(map(str, re[::-1])))
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    data_1 = solution(data)
    data_2 = solution(data_1)
    data_3 = solution(data_2)

    result = [data_1, data_2, data_3]
    real = [[0]*3 for _ in range(N)]

    for i in range(N):
        for j in range(3):
            real[i][j] = result[j][i]

    print('#{}'.format(tc))
    for k in real:
        print(*k)