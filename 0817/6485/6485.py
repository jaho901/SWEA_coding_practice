import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dic = [0]*5000

    for i in range(N):  # 딕셔너리에 way 범위에 해당되는 value값 1씩 늘리기
        s, e = map(int, input().split())
        for j in range(s, e + 1):
            dic[j] += 1

    P = int(input())
    result = []

    for i in range(P):  # result 리스트에 해당 정류장에 맞는 value값 저장
        result.append(dic[int(input())])
    result = ' '.join(map(str, result))
    print('#{} {}'.format(tc, result))
