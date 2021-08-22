import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = []

    # str1에 들어있는 각각의 알파벳들의 개수를 cnt 리스트에 추가
    for i in str1:
        cnt.append(str2.count(i))
    
    # 그 값들 중에서의 max값을 반환
    maximum = max(cnt)
    print('#{0} {1}'.format(tc, maximum))
