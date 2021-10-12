import sys
sys.stdin = open('10726.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    # N번 만큼 반복해서 조사할 건데,
    # 한번이라도 0이 나오면 OFF
    # 모두 1이어야 한다 -> 한 개라도 0이면 OFF
    flag = 1
    for i in range(N):
        print(M & (1<<i))
        if M & (1<<i) == 0:
            flag = 0
            break
    print(flag)
    if flag:
        print('#{} {}'.format(tc, 'ON'))
    else:
        print('#{} {}'.format(tc, 'OFF'))


