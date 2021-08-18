import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # min, max 내장함수 사용
    '''
    maximum = max(numbers)
    minimum = min(numbers)
    result = maximum - minimum
    '''

    # 내장함수 사용 XX

    maximum = 0
    for i in numbers:
        if maximum < i:
            maximum = i
    minimum = maximum
    for i in numbers:
        if minimum > i:
            minimum = i

    result = maximum - minimum

    print('#{0} {1}'.format(tc, result))