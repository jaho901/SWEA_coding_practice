T = int(input())
for tc in range(1, T+1):
    N = 5
    arr = [list(input()) for _ in range(N)]

    max_length = 0
    for i in arr:
        if max_length < len(i):
            max_length = len(i)

    for j in range(len(arr)):
        if len(arr[j]) < max_length:
            for k in range(max_length - len(arr[j])):
                arr[j].append('')

    arr_2 = []
    for re in zip(*arr):
        arr_2.append(''.join(re))

    result = ''.join(arr_2)

    print('#{} {}'.format(tc, result))