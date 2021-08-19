import sys
sys.stdin = open('input.txt')

def solution(N):
    global total
    result = 0
    r_number = sorted(number, reverse=True)

    if number == r_number:
        return 0
    else:
        for i in range(N):
            maximum = max(number)
            if number[i] != maximum:
                total.append(number[i])
            elif number[i] == maximum:
                for j in range(len(total)):
                    result += abs(total[j] - number[i])
                total = []
            number[i] = 0
        return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    print(number)
    total = []

    print('#{} {}'.format(tc, solution(N)))





