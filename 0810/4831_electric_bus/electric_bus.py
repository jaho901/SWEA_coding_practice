import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 종점인 정류장
    # K : 한 번 충전으로 이동할 수 있는 최대 정류장 수
    # M : 충전기가 설치된 정류장의 수
    # number : 충전기가 설치된 정류장 번호
    # 충전기 설치가 잘못되어 종점 도착 못하는 경우 0 반환
    # 0을 벗어났을 때 충전은 완충 but 충전 횟수에 포함은 안함
    K, N, M = map(int, input().split())
    number = list(map(int, input().split()))
    number.insert(0, 0)
    number.insert(len(number), N)

    # 각 정류장 번호의 차이를 구한 리스트를 얻음
    # 그 차이가 K보다 크면 0을 반환 아니면 밑에 if문으로 ㄱㄱ
    diff = []
    for i in range(len(number) - 1):
        diff.append(number[i + 1] - number[i])


    # 차이가 K보다 작을 경우
    if max(diff) <= K:
        pos = []
        result = 0
        now = 0

        # max_idx가 N이랑 같아진 경우 종료
        while now != N:
            # 계속해서 max_idx값에 K씩 더해준다.
            now += K
            # 여기서 반복문을 돌려준다.
            for i in range(len(number)):
                # 만약 number의 요소가 max_idx보다 작거나 같으면
                if now >= number[i]:
                    # pos라는 리스트에 값을 더해준다.
                    pos.append(number[i])
            # 그 중에서의 최댓값을 max_idx로 초기화시켜주며
            now = max(pos)
            # result값을 1씩 증가시켜준다.
            result += 1

        # 이 경우 출발점에서부터 시작하므로 출발점에서는 항상 충전이 풀이기 때문에
        # 1을 빼줌으로써 정확한 result값을 반환하게 된다.
        result = result - 1

    # 만약 정류장과 정류장 사이의 길이가 K보다 긴 경우 0을 반환한다.
    else:
        result = 0

    print('#{0} {1}'.format(tc, result))







