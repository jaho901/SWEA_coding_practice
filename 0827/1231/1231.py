import sys
sys.stdin = open('input.txt')

def in_order(n):
    if n:
        in_order(left[n])
        result.append(word[n])
        in_order(right[n])

T = 10
for tc in range(1, T+1):

    N = int(input())

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    word = [0] * (N + 1)

    for n in range(1, N + 1):
        a = list(input().split())
        word[n] = a[1]
        if len(a) >= 3:
            if len(a) > 3:
                right[n] = int(a[3])
            left[n] = int(a[2])

    result = []
    in_order(1)

    print('#{}'.format(tc), end=' ')
    print(''.join(result))
'''
########
def inorder(cur=1):  # 왼, 부, 오
    if cur > N:
        return

    inorder(2 * cur)
    print(char[cur], end='')
    inorder(2 * cur + 1)

for k in range(1, 11):
    N = int(input())
    temp = [input().split() for i in range(N)]  # 일단 입력 받아
    char = [0 for i in range(N + 1)]  # 노드 번호마다 문자 매치
    for i in range(len(temp)):
        char[int(temp[i][0])] = temp[i][1]
    print('#{}'.format(k), end=' ')
    inorder()
    print()

