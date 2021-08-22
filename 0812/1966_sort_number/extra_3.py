T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(N-1):
        minimum = data[i]
        idx = i
        for j in range(i+1, N):
            if minimum > data[j]:
                minimum = data[j]
                idx = j
        data[i], data[idx] = data[idx], data[i]

    data = ' '.join(map(str, data))
    print('#{} {}'.format(tc, data))