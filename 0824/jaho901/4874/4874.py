import sys
sys.stdin = open('input.txt')
'''
T = int(input())
for tc in range(1, T+1):
    data = list(input().split())
    stack = []
    num = 0
    ope = 0

    for i in range(len(data)):
        if data[i].isdigit() == True:
            stack.append(int(data[i]))
        elif data[i] in '+-*/':
            try:
                x = stack.pop()
                y = stack.pop()
            # 이 경우를 넣은 이유는 숫자가 stack에 1개만 들어있는데 2개를 pop할경우
            # 인덱스 에러가 나기 때문에 try ~ except를 넣어주었다.
            except IndexError:
                print('#{} {}'.format(tc, 'error'))
                break
            if data[i] == '+':
                stack.append(y + x)
            elif data[i] == '-':
                stack.append(y - x)
            elif data[i] == '*':
                stack.append(y * x)
            elif data[i] == '/':
                stack.append(y // x)
        elif data[i] == '.':
            # 정확하게 계산된 경우는 오로지 stack에 계산된 마지막 값 하나만 남은 경우니깐
            # 아래와 같은 조건문을 넣어준다.
            if len(stack) == 1:
                print('#{} {}'.format(tc, stack[-1]))
            # 그 외에도 숫자가 연산자보다 더 많은 경우 제대로 계산이 되지 않았기 때문에
            # error를 반환한다.
            else:
                print('#{} {}'.format(tc, 'error'))
'''
T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    # print(arr)

    stack = []
    result = ''

    #숫자 구분
    for i in range(len(arr)):
        if arr[i].isdigit():
            stack.append(arr[i])
        else:
            try:
                # 맨 밑에 and stack[-1] == '.'이 있으면
                # 무조건 stack의 길이는 2가 되기 때문에
                # if문이 돌아가지 않아서 위에다가 옮긴거
                if arr[i] == '.':
                    break
                # 위에서 받아올 때 str로 받아와서
                # 이렇게 인트로 변경해주고 계산시작
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                # 연산자 구분
                if arr[i] == '+':
                    result = num2 + num1
                elif arr[i] == '-':
                    result = num2 - num1
                elif arr[i] == '*':
                    result = num2 * num1
                elif arr[i] == '/':
                    result = num2 / num1
                stack.append(result)
            except:
                pass
    # print(result)
    if len(stack) == 1:
        print('ok')
    else:
        print('error')


