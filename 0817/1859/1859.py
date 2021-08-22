T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    data = data[::-1]
    result = 0
    sub = []

    maximum = max(data)
    i = len(data) - 1

    while data:
        a = data.pop()
        if a != maximum:
            sub.append(a)
        elif a == maximum:
            for j in range(len(sub)):
                result += a - sub[j]
            if data:
                maximum = max(data)
            sub = []

    print('#{} {}'.format(tc, result))