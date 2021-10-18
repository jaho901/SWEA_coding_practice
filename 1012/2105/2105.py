import sys
sys.stdin = open('2105.txt')
from itertools import combinations_with_replacement

# 현재 위치에서 카페 투어가 가능한지의 여부 확인
def check(i, j, box):
    # result값을 계속해서 변경해주기 위해 global로 불러옴
    global result
    # 아래의 반복문의 종료여부를 확인하기 위해 생성
    turn = False
    # 같은 종류의 디저트를 먹었는지의 여부를 확인하기 위해 set 생성
    desert = set()
    # 현재위치 삽입
    desert.add(arr[i][j])

    # 총 4가지 방향으로 (대각선) 이동
    for k in range(4):
        n1, n2 = box[0], box[1]
        # 각각의 방향에서 box에 주어진 방향까지 쭉 이동하기 위해 while문 생성
        while True:
            ni, nj = i + dx[k], j + dy[k]
            # 처음과 3번째는 box[0]번씩 이동해야하고,
            if k % 2 == 0:
                # 이동이 가능하다면
                if 0 <= ni < N and 0 <= nj < N:
                    # set에 현재 디저트 종류 추가하고 현재위치 변경
                    desert.add(arr[ni][nj])
                    n1 -= 1
                    i, j = ni, nj
                    # 총 box[0]번을 이동했다면 while문 종료
                    if n1 == 1:
                        break
                # 만약에 이동이 불가능하면 현재위치에서 이 방법은 틀린방법이기 때문에 check함수 자체를 종료
                else:
                    turn = True
                    break

            # 2번째와 4번재는 box[1]번씩 이동해야한다.
            else:
                if 0 <= ni < N and 0 <= nj < N:
                    desert.add(arr[ni][nj])
                    n2 -= 1
                    i, j = ni, nj
                    if n2 == 1:
                        break
                else:
                    turn = True
                    break
        # while문에서 중간에 종료된거라면 for문 또한 종료
        if turn:
            break

    # 만약에 set의 길이와 주어진 카페투어 거리가 다르면 투어 불가능하기 때문에 Fasle 반환
    if len(desert) != (box[0]+box[1])*2 - 4:
        return False
    # 만약에 같으면 값을 비교하고 result값 변경
    else:
        if len(desert) > result:
            result = len(desert)
        return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    result = 0
    # 일반적인 combinations는 중복이 없는 조합이라서 (2, 3)의 값만 가지지만
    # combinations_with_replacement는 중복조합이라서 (2, 2)와 (2, 3)을 가진다.
    # 여기서 중복조합이란 (a, b)에서 a==b인 경우도 존재한다는 의미!!
    boxes = list(combinations_with_replacement(range(2, N), 2))
    # 마지막 값은 항상 존재하지 않으므로 제거!!
    boxes.pop()

    # 그리고 (a, b)가 존재하고 a와 b가 다른경우에는 (b, a)도 존재해야하기 때문에
    # 새로 생성하여 boxes에 넣어줌
    for i in range(len(boxes)):
        if boxes[i][0] != boxes[i][1]:
            boxes.append((boxes[i][1], boxes[i][0]))

    # 그리고 a와 b 모두 내림차순으로 정렬시켜주었습니다.
    # 이유 -> 최대값을 구하는 문제이기 때문!!
    boxes = sorted(boxes, key=lambda x:(-x[0], -x[1]))
    # print(boxes)
    exist = True
    # 만약 투어길이 존재하지 않는 경우 -1을 반환해야하기 때문에 초기값 -1 지정
    result = -1

    for i in range(N):
        for j in range(N):
            if boxes:
                length = len(boxes)
                cnt = 0
                a = []
                # boxes 값을 계속해서 줄여줌으로써 시간복잡도를 줄여주었다.
                while True:
                    # check함수로 가능여부를 확인했을 때 같은 길이의 값이 하나라도 존재하면
                    # 다른 위치에서 같은 경로로 이동할 필요가 없기 때문에 a에 담아 제거
                    if check(i, j, boxes[cnt]):
                        a.append(cnt)
                    cnt += 1
                    if cnt == length:
                        break
                # 만약 a가 존재할 때는 인덱스를 반대로 해서 pop해주었다.
                # 만약 정방향으로 이동한다면 indexerror 발생
                if a:
                    for b in range(len(a)-1, -1, -1):
                        boxes.pop(a[b])
            # 만약 i, j가 N-1, N-1까지 안가더라도 중간에 box가 다 사라진다면
            # 투어길을 확인할 필요가 없기 때문에 반복문 모두 종료!
            else:
                exist = False
                break
        if not exist:
            break

    print('#{} {}'.format(tc, result))
