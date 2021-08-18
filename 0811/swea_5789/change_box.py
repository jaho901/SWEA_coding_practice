
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    l1, r1 = map(int, input().split())
    l2, r2 = map(int, input().split())

    box = [0]*N
    print(box)

    for i in range(l1-1, r1):
        box[i] = 1
    for j in range(l2-1, r2):
        box[j] = 2

    result = ' '.join(map(str, box))

    print('#{0} {1}'.format(tc, result))











