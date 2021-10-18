import sys
sys.stdin = open('4012.txt')
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    S_comb = list(combinations(range(N), N//2))
    length = len(S_comb[0])
    result = 10000000

    for x in S_comb:  # a 음식 고를 식재료 선택
        y = [i for i in range(N) if i not in x]  # a 음식에서 선택하지 않은 식재료 선택
        a, b = 0, 0
        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                a += arr[x[i]][x[j]] + arr[x[j]][x[i]]  # a 음식의 맛 더하기
                b += arr[y[i]][y[j]] + arr[y[j]][y[i]]  # b 음식의 맛 더하기

        result = min(result, abs(a - b))  # 최소값으로 갱신

    print('#{} {}'.format(tc, result))