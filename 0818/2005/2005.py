import sys
sys.stdin = open('input.txt')
'''
def pascal(cur):
    for i in range(1, cur+1):
        if i <= 2:
            n_list = [1] * i
            print(*n_list)
        else:
            num = []
            for j in range(1, i-1):
                num.append(n_list[j - 1] + n_list[j])
            n_list = [1] + num + [1]
            print(*n_list)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    pascal(N)
'''

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input()) + 1
    arr = [[0] * N for _ in range(N)]
    for i in range(1, N):
        for j in range(1, i+1):
            if i <= 2:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    result = []
    for i in range(1, N):
        sub = []
        for j in range(1, N):
            if arr[i][j] != 0:
                sub.append(arr[i][j])
        result.append(sub)

    print('#{}'.format(tc))
    for i in result:
        print(*i)
'''
