import sys
import math
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))




    num = 0
    while num != N:
        max_value = max(numbers)
        min_value = min(numbers)
        max_idx = numbers.index(max_value)
        min_idx = numbers.index(min_value)
        numbers[max_idx] -= 1
        numbers[min_idx] += 1

        num += 1

    '''
    for i in range(0, N):
        a = max(numbers)
        b = min(numbers)
        a_idx = numbers.index(a)
        b_idx = numbers.index(b)
        numbers[a_idx] -= 1
        numbers[b_idx] += 1
    '''

    print('#{0} {1}'.format(tc, max(numbers) - min(numbers)))