# import sys
# sys.stdin = open('5174.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    b = ''
    for i in range(N):
        a = int(M[i], 16)
        b_2 = str(bin(a))
        # print(b_2)

        b_2 = b_2.lstrip('0b')
        if len(b_2) == 4:
            b += b_2
        else:
            zero = 4 - len(b_2)
            b_2 = '0'*zero + b_2
            b += b_2
    print('#{} {}'.format(tc, b))