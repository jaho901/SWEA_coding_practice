import sys
sys.stdin = open('input.txt')


def make_arr(number):
    arr = [[0] * 100 for _ in range(100)]
    for j in range(len(number)//2):
        arr[number[j*2]][number[j*2 + 1]] = 1
    return arr


def solution(arr):
    visited = [0]*100
    i = 0
    stack = []
    visited[i] = 1
    while i != len(arr[0]) + 1:
        for w in range(len(arr[0])):
            if arr[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                if i == 99:
                    return 1
                visited[i] = 1
                break

        else:
            if stack:
                i = stack.pop()
            else:
                i = len(arr[0]) + 1
                return 0


T = 10
for Tc in range(1, T+1):
    tc, N = map(int, input().split())
    number = list(map(int, input().split()))

    arr = make_arr(number)

    print('#{} {}'.format(tc, solution(arr)))