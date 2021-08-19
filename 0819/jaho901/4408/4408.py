import sys
sys.stdin = open('input.txt')





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    cnt = 1
    room_idx = [1] * len(room)
    room_idx[0] = 0

    for i in range(N):
        for j in range(i+1, N):
            if room[i][0] <= room[j][0] <= room[i][1] or room[i][0] <= room[j][1] <= room[i][1]:
                if room_idx[j] == 0:
                    continue
                else:
                    cnt += 1
                    room_idx[j] = 0
        if sum(room_idx) == 0:
            break
    print('#{} {}'.format(tc, cnt))


