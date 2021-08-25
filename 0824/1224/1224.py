import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(input())
    # print(data)

    operator = {
        '(' : 0,
        '+' : 1,
        '*' : 2,
    }

    stack = []
    fomula = ''

    for i in data:
        if i.isdigit() == True:
            fomula += i
        else:
            if i == '(':
                stack.append(i)

            elif i in operator:
                while operator[i] <= operator[stack[-1]]:
                    fomula += stack.pop()
                stack.append(i)


            elif i == ')':
                while stack and stack[-1] != '(':
                    fomula += stack.pop()
                stack.pop()

    while stack:
        fomula += stack.pop()


    for j in fomula:
        if j not in operator.keys():
            stack.append(int(j))
        else:
            x = stack.pop()
            y = stack.pop()
            if j == '+':
                stack.append(y+x)
            elif j == '*':
                stack.append(y*x)
    print('#{} {}'.format(tc, stack[0]))














