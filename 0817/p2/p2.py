import sys
sys.stdin = open('input.txt')


# 회문을 찾는 함수를 만들었습니다.
def is_palindrome(arr):
    result = []
    # 첫 번째 행에 있는 값에서
    for i in arr:
        # 해당 열에서 주어진 M의 길이만큼 for문을 반복
        for j in range(N - M + 1):
            str1 = i[j:j+M]
            if str1 == str1[::-1]:
                result.append(str1)
                break
        if len(result) > 0:
            break
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())


    string = [input() for _ in range(N)]


    '''
    # 인덱스 i와 j를 바꾼 행렬 들고오기
    h_string = []
    for i in range(len(string)):
        sub = ''
        for j in range(len(string[0])):
            sub += string[j][i]
        h_string.append(sub)

    result1 = is_palindrome(string)
    result2 = is_palindrome(h_string)

    if result1:
        print('#{0} {1}'.format(tc, ''.join(*result1)))
    else:
        print('#{0} {1}'.format(tc, ''.join(*result2)))
    '''






    # 관이형 코드 ==> zip(*args) 사용
    # 열을 불러올 수 있는 쉬운 방법

    # 최종 결과 반환 리스트
    result = []

    # zip(*args)는 배열에서 행이 아닌 열을 순서대로 가져올 수 있게 해주는 함수로 활용가능
    for re in zip(*string):
        # 세로줄을 모두 str_list에 넣어주고 한번만 비교하면 된다.
        string.append(''.join(re))

    result1 = is_palindrome(string)

    print('#{0} {1}'.format(tc, ''.join(*result1)))



    '''
    ## 영남이 코드 => global 변수를 불러옴으로써 조금이라도 시간복잡도 해결
    
    def is_pal(arr):  # M글자의 회문 존재여부 판단함수, 존재할경우 회문, 아닐경우 0리턴
        ans = 0
        global flag
        for i in range(len(arr)):
            for j in range(len(arr[i]) - M + 1):
                word = arr[i][j:j + M]
                if word == word[::-1]:
                    ans = word
                    flag = 1
                    break
            # i의 반복문도 바로 break 시켜준다.
            if flag:
                break
        return ans


    for k in range(1, n + 1):
        N, M = map(int, input().split())
        arr = [input() for i in range(N)]
        flag = 0
        # 가로 탐색
        w = is_pal(arr)
        if w:
            print('#{} {}'.format(k, w))

        # 세로탐색
        # 만약에 가로에서 회문을 찾아 flag가 1인 경우
        # 더 이상 연산 안하도록 지정
        if not flag:
            temp = [''] * N
            for i in range(len(arr)):  # 세로를 가로로 바꾸기
                for j in range(len(arr)):
                    temp[j] += arr[i][j]

            print('#{} {}'.format(k, is_pal(temp)))
    '''




