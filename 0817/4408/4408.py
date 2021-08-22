T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [0] * 200
    for i in range(N):
        a, b = map(int, input().split())
        if a < b:
            for j in range((a-1)//2, (b-1)//2+1):
                result[j] += 1
        elif a > b:
            for j in range((b-1)//2, (a-1)//2 + 1):
                result[j] += 1

    # print(result)
    print('#{} {}'.format(tc, max(result)))