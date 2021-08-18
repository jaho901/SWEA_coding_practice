import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    length = len(number)
    # 연속되는 M개의 수의 합을 담을 리스트 생성
    summation = [0] * (length-(M-1))
    print(summation)

    # 반복문 사용
    # range는 0부터 길이에서 (M-1)을 뺀 수로 지정
    for i in range(length-(M-1)):
        # 지정된 인덱스 i부터 M개 까지의 합을 구함
        summation[i] += sum(number[i:i+M])

    # 각각의 연속된 M개의 수의 합을 담은 리스트에서 최댓값과 최솟값의 차를 result에 저장
    result = max(summation) - min(summation)

    print('#{0} {1}'.format(tc, result))
