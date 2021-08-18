import sys
sys.stdin = open('input.txt')


def is_palindrom(arr):
    # global ans를 들고옴으로써 계속해서 ans를 변경해준다.
    global ans
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(j, len(arr[i])): # k를 j부터 시작해서 그 행의 끝까지 비교
                result1 = arr[i][j:k + 1]
                # 만약에 그 결과가 reverse 시킨 결과와 동일한 경우
                if result1 == result1[::-1]:
                    # 그 길이를 temp에 저장해주고
                    temp = len(result1)
                    # global ans와 계속해서 비교해주면서 가장 긴 값을 ans로 저장
                    if ans < temp:
                        ans = temp
    return

T = 10
for tc in range(1, T+1):
    N = int(input())
    M = 100
    str_arr = [list(input()) for _ in range(M)]

    ans = 0

    # 회문1과 동일한 방법으로 세로를 확인하기 위해 새로운 array 생성
    hstr_arr = []
    for l in range(len(str_arr)):
        sub = []
        for m in range(len(str_arr[0])):
            sub.append(str_arr[m][l])
        hstr_arr.append(sub)

    # 가로
    is_palindrom(str_arr)
    # 세로
    is_palindrom(hstr_arr)

    # 함수를 돌린것으로 가로와 새로 모두 비교 이후 가장 큰 값이 ans에 저장이 되어있을 것이다.

    print('#{0} {1}'.format(tc, ans))


    '''
    for i in range(len(str_arr)):
        for k in range(len(str_arr[0])):
            for j in range(k, len(str_arr[0])):
                n = (j+1)//2    # 5
    #             if str_arr[i][k:n] == list(reversed(str_arr[i][(j+2)//2:j+1])):
    #                 result1.append(str_arr[i][k:j+1])
                if str_arr[i][k:n] == list(reversed(str_arr[i][k:j+1]))[k:n]:
                    result1.append(str_arr[i][k:j+1])
    print(result1)
    '''



