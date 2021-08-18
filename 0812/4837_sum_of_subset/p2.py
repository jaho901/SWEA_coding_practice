import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 1부터 12까지의 숫자를 가진 집합 A 생성
    set_A = list(range(1, 13))

    length = len(set_A)

    # 모든 부분집합을 넣을 리스트 생성
    set = []

    # 부분집합으로 ㄱㄱ
    for i in range(1<<length):
        # i가 바뀔대마다 부분집합 리스트를 초기화시킴
        subset = []
        for j in range(length):
            if i & (1<<j):
                subset.append(set_A[j])
        # i가 바뀌기 전에 전체 리스트에 부분집합 리스트를 추가해준다.
        set.append(subset)

    # 가장 앞에 리스트에 공집합인 0을 넣어준다.
    set[0].append(0)

    # 최종 결과값 지정
    result = 0

    # 전체 리스트에서 각각의 부분집합 중
    # 길이가 N이고, 합이 K인 부분집합이 존재하면 result에 1씩 더해준다.
    for i in set:
        if len(i) == N and sum(i) == K:
            result += 1

    print('#{0} {1}'.format(tc, result))
