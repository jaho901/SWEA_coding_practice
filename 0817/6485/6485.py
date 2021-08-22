T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [0] * 5001
    for n in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            result[i] += 1


    P = int(input())
    C_list = []
    for i in range(P):
        C_list.append(result[int(input())])
    C_list = ' '.join(map(str, C_list))
    print('#{} {}'.format(tc, C_list))