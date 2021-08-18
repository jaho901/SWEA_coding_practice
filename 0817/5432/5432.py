import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stick = list(input())
    length = len(stick)

    new_stick = []
    i = 0

    while i < length:
        if stick[i] == '(' and stick[i+1] == ')':
            new_stick.append('1')
            i += 2
        else:
            new_stick.append(stick[i])
            i += 1

    s, e = 0, 0
    cnt = 0

    for i in new_stick:
        m = s - e
        if i == '(':
            s += 1
        elif i == ')':
            cnt += 1
            e += 1
        if m == 0:
            pass
        else:
            if i == '1':
                cnt += m

    print('#{} {}'.format(tc, cnt))


