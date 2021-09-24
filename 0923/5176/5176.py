import sys
sys.stdin = open('5176.txt')

def binary(n):
    global count
    if n <= N:
        # 가장 먼저 2^n승부터 1의 값넣는다.
        binary(n*2)
        tree[n] = count
        # 그 이후 2^n + 1의 값에 2부터 1씩 증가하는 값들을 넣어준다.
        count += 1
        binary(n*2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 0부터 N까지의 값을 넣을 tree 데이터 생성
    tree = [0 for _ in range(N+1)]
    count = 1
    binary(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))

