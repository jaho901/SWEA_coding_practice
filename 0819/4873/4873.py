import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    string = list(input())

    i = 0
    while True:
        # 현재위치의 단어와 다음위치의 단어가 동일한 경우
        if string[i] == string[i+1]:
            # 현재위치의 단어와 다음위치의 단어를 제거
            string.pop(i)
            string.pop(i)
            # 동시에 인덱스를 0으로 초기화
            i = 0
        
        # 그 외의 경우 인덱스를 1씩 추가해줌
        else:
            i += 1

        # 계속 제거해주다가 제거못해주고 결국 string의 끝까지 가게되면 break
        length = len(string)
        if i >= length-1:
            break

    # 반복문자 제거 이후 남은 문자열 길이저장
    min_len = len(string)

    print('#{} {}'.format(tc, min_len))


    '''
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
        elif char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))
    '''
