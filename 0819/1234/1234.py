import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, string = map(int, input().split())
    string = str(string)

    stack = []
    for char in string:
        if not stack:
            stack.append(char)
        elif char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    if stack[0] == '0':
        stack = stack[1:]
    stack = ''.join(stack)
    print('#{} {}'.format(tc, stack))








