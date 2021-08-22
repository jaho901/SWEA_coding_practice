def solution(arr):
    global N
    global M
    result = 0
    for k in range(1, N + 1):
        for j in range(1, N - M + 2):
            # 전과 M번째 후가 0일때
            if arr[k][j - 1] == 0 and arr[k][j + M] == 0 and sum(arr[k][j:j + M]) == M:
                result += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(arr)):
        arr[i].insert(0, 0)
        arr[i].append(0)
    arr.insert(0, [0]*(N+2))
    arr.append([0]*(N+2))

    arr_2 = []
    for re in zip(*arr):
        arr_2.append(list(re))

    a = solution(arr)
    b = solution(arr_2)
    print('#{} {}'.format(tc, a + b))