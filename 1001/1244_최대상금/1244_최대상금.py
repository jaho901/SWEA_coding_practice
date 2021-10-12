import sys
sys.stdin = open('input.txt')

def perm(s, M):
    global result
    val = int(''.join(cards))
    if val in visited:
        return
    visited.append(val)

    if s == M:
        if val > result:
            result = val
        return

    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            cards[j], cards[i] = cards[i], cards[j]
            perm(s+1, M)
            cards[j], cards[i] = cards[i], cards[j]

T = int(input())

for tc in range(1, T+1):
    arr = input().split()
    cards, M = list(arr[0]), int(arr[1])
    result = int(arr[0])
    visited = []
    perm(0, M)
    print(result)
