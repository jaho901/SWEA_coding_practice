import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(input())
    operator = {
        '+':1,
        '-':1,
        '*':2,
        '/':2
    }
    # print(operator['*'])
    sub = ''
    stack = []

    for i in data:
        if i in operator.keys():
            if stack:
                if operator[i] >= operator[stack[-1]]:
                    stack.append(i)
                else:
                    while stack:
                        sub += stack.pop()
                    stack.append(i)
            else:
                stack.append(i)

        else:
            sub += i
    while stack:
        sub += stack.pop()

    for j in sub:
        if j not in operator.keys():
            stack.append(int(j))
        else:
            x = stack.pop()
            y = stack.pop()
            if j == '+':
                stack.append(y+x)
            elif j == '-':
                stack.append(y-x)
            elif j == '*':
                stack.append(y*x)
            elif j == '/':
                stack.append(y/x)
    print('#{} {}'.format(tc, stack[0]))
