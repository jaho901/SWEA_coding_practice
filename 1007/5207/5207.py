import sys

sys.stdin = open('5207.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_N = list(map(int, input().split()))
    num_N = sorted(num_N)
    num_M = list(map(int, input().split()))

    cnt = 0
    for num in num_M:
        s,e = 0, N-1
        flag = 0

        while s <= e:
            mid = (s + e)//2
            if num >= num_N[mid]:
                if num == num_N[mid]:
                    cnt += 1
                    break

                s = mid + 1
                if flag == 1:
                    break
                flag = 1

            elif num < num_N[mid]:
                e = mid - 1
                if flag == -1:
                    break
                flag = -1


    print('#{} {}'.format(tc, cnt))