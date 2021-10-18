import sys

sys.stdin = open('5203.txt')

def check(player_1, player_2):
    global result
    result1 = baby_jin(player_1)
    result2 = baby_jin(player_2)
    if result1 > result2:
        result = 1
        return True
    elif result1 < result2:
        result = 2
        return True

def baby_jin(player):
    result = 0
    for i in range(10):
        if player[i] >= 3:
            result += player[i]//3

    for j in range(8):
        if player[j] and player[j+1] and player[j+2]:
            if player[j] == 2 and player[j+2] == 2 and player[j+3]==2:
                result += 2
            else:
                result += 1
    return result


T = int(input())
for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    player_1 = [0] * 10
    player_2 = [0] * 10
    result = 0
    for i in range(12):
        if i%2 == 0:
            player_1[card[i]] += 1
        else:
            player_2[card[i]] += 1

        if check(player_1, player_2):
            break

    print('#{} {}'.format(tc, result))