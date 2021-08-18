import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    sort_number = []

    for i in range(N-1):
        minimum = number[i]
        for j in range(i+1, N):
            if minimum > number[j]:
                minimum = number[j]
                number[i], number[j] = number[j], number[i]

    result = ' '.join(map(str, number))
    print('#{0} {1}'.format(tc, result))


