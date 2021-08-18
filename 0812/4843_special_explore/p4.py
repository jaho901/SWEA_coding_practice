import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    number = sorted(number)

    n = 10/2
    result = []
    i = 0

    while n > 0:
        # 인덱스를 보면 N-0, 0, N-1, 1, N-2, 2, --- , N-4, 4 => 10개
        result.append(number[N-1-i])
        result.append(number[i])
        i += 1
        n -= 1

    result = " ".join(map(str, result))
    print('#{0} {1}'.format(tc, result))


