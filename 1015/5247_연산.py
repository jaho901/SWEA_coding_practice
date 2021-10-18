import sys
sys.stdin = open('input_5247.txt','r')


#
#
# def calc(n, idx):
#     if idx == 0: return n + 1
#     elif idx == 1: return n - 1
#     elif idx == 2: return n * 2
#     else: return n - 10
#
#
# def BFS():
#     Q = [0] * 1000000
#     front = rear = -1
#
#     rear += 1
#     Q[rear] = N
#     memo[N] = 0
#
#     while front != rear:
#         front += 1
#         num = Q[front]
#
#         if num == M: #지금 뽑은 값이 M과 같다면 해당 횟수를 반환한다.
#             return memo[num]
#
#         for i in range(4):
#             next_num = calc(num, i)
#             # 중간 연산 결과는 100만이하의 자연수
#             if 0 < next_num <= 100000 and memo[next_num] == -1:
#                 memo[next_num] = memo[num] + 1
#                 rear += 1
#                 Q[rear] = next_num
#
#     return -1
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) #  N!=M  , N, M 100만 이하의 자연수이다.
#
#     memo = [-1] * 1000001
#
#     print("#{} {}".format(tc, BFS()))


######################################################

from collections import deque

def BFS():
    Q = deque()
    Q.append(N)
    memo[N] = True

    ans = 0

    while Q:
        size = len(Q)

        for i in range(size):
            num = Q.popleft()
            if num == M: return ans

            for j in (num+1, num-1, num*2, num-10):
                if 0 < j <= 1000000 and not memo[j]:
                    memo[j] = True
                    Q.append(j)

        ans += 1




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #  N!=M  , N, M 100만 이하의 자연수이다.

    memo = [False] * 1000001

    print("#{} {}".format(tc, BFS()))
