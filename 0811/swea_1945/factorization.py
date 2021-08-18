import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    number = int(input())

    result = [0]*5

    while number != 1:
        if number%2 == 0:
            result[0] += 1
            number = number//2
        elif number%3 == 0:
            result[1] += 1
            number = number // 3
        elif number%5 == 0:
            result[2] += 1
            number = number // 5
        elif number%7 == 0:
            result[3] += 1
            number = number // 7
        elif number%11 == 0:
            result[4] += 1
            number = number // 11

    a = ' '.join(map(str, result))
    print('#{0} {1}'.format(tc, a))
