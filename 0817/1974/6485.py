import sys
sys.stdin = open('input.txt')

t = int(input())

for idx in range(1, t+1):
    # 스도쿠 판 받아와서 만들기
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))

    answer = 1

    # 3 * 3 작은 격자 9개 만들기
    square = [[[] for _ in range(3)] for _ in range(3)]
    for i in range(9):
        garo = []   # 가로 줄
        sero = []   # 세로 줄
        for j in range(9):
            # 만약 검토하려는 숫자가 이미 가로 또는 세로 도는 작은 격자 안에 있다면 0. 바로 중단
            if (board[i][j] in garo) or (board[j][i] in sero) or (board[i][j] in square[i//3][j//3]):
                answer = 0
                break

            # 검토할 숫자가 가로 또는 세로 또는 작은 격자에 없다면 (겹치는게 아니라면) 추가
            garo.append(board[i][j])
            sero.append(board[j][i])
            square[i//3][j//3].append(board[i][j])

        # 이미 겹치는 숫자가 있었다면 중단
        if not answer:
            break

    print('#{} {}'.format(idx, answer))


    '''
    def solution(data):
    global result
    result1 = 0
    for x in range(len(data)):
        for y in range(len(data)):
            num = data[x][y]
            if result[num] == 0:
                result[num] += 1
        if sum(result) == 9:
            result1 += 1
        result = [0] * 10
    return result1

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = [0] * 10


    # 가로
    result_4 = solution(data)

    # 세로
    data2 = []
    for re in zip(*data):
        data2.append(list(re))
    result_2 = solution(data2)

    # 한칸한칸
    result_3 = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(0, 3):
                for l in range(0, 3):
                    a = data[i+k][j+l]
                    if result[a] == 0:
                        result[a] += 1
            if sum(result) == 9:
                result_3 += 1


    if result_4 + result_2 + result_3 == 27:
        total = 1
    else:
        total = 0

    print('#{} {}'.format(tc, total))
    '''