import sys
sys.stdin = open('input.txt')


def solution(string):
    result = []
    for i in string:
        if i == '(' or i == '{':
            result.append(i)

        elif i == ')' or i == '}':
            # result가 존재하면 즉, 여는 괄호가 있으면 삭제
            if result:
                p = result.pop()  # p == 여는 괄호
            # 여는 괄호가 없으면 잘못됬으니 0 반환
            else:
                return 0

            # (} or {) 의 형태가 나올 경우도 잘못됬으니 0 반환
            if p == '(' and i == '}':
                return 0
            elif p == '{' and i == ')':
                return 0

    # result가 존재한다면
    if result:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    string = list(input())

    print('#{} {}'.format(tc, solution(string)))