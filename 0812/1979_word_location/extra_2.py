import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # 조건을 생각해보자
    # 조건 1. 연속으로 3개가 1인경우
    # 조건 2. 상하가 0 또는 좌우가 0
    # -> 상하인 경우와 좌우인 경우 따로 생각?
    # 함칠수는 없을까...

    # 못품
    for i in range(N):
        cnt = 0
        for j in range(N):
            # puzzle이 1이면 카운트를 1씩 추가해준다.
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                    cnt = 0






