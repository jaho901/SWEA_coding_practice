import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    '''
    # 가장 간단하게 str1이 str2에 존재한다면 1을 반환,  아니면 0을 반환
    if str1 in str2:
        result = 1
    else:
        result = 0
    '''

    # 브루트 포스
    result = 0
    i = 0
    j = 0
    while i < len(str2) and j < len(str1):
        if str1[j] != str2[i]:  # 일치하지 않으면 j=0, i는 처음 인덱스 +1로 이동
            i = i - j
            j = -1
        i += 1
        j += 1
        # j == 찾고자하는 단어의 길이
        if j == len(str1):
            result += 1
            break

    print('#{0} {1}'.format(tc, result))












