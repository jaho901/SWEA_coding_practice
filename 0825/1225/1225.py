import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))

    # 현재 진행중인 사이클에서
    # 빼야할 값의 크기를 알고 있어야 한다.
    cnt = 1
    while data[-1] > 0:
        # 한 사이클은 5까지 빼는게 한 사이클
        # 빼고자 하는 값의 크기가 5 초과가 되면
        # 다시 1로 돌아가야 한다.
        if cnt == 6:
            cnt = 1
        data.append(data.pop(0) - cnt)
        cnt += 1
    data[-1] = 0
    data = ' '.join(map(str, data))
    print('#{} {}'.format(tc, data))


