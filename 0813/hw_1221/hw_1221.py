import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, length = map(str, input().split())
    string = list(input().split())

    # 숫자 체계
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # string에서 number 각각이랑 동일하면 그 number의 인덱스로 교체 ex) 'ZRO'이면 0으로 바꾸기
    for i in range(int(length)):
        for j in range(len(number)):
            if string[i] == number[j]:
                string[i] = number.index(number[j])
    string = sorted(string)

    result = []
    
    # 이번에는 인덱스를 해당하는 문자로 변경
    for i in range(int(length)):
        result.append(number[int(string[i])])

    print(N)
    print(' '.join(result))



