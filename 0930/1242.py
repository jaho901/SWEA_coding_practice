import sys
sys.stdin = open('1242.txt')

T = int(input())
makeT = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}
def mT(length, sub):
    b = ''
    for i in range(length):
        a = int(sub[i], 16)
        b_2 = str(bin(a))

        b_2 = b_2.lstrip('0b')
        if len(b_2) == 4:
            b += b_2
        else:
            zero = 4 - len(b_2)
            b_2 = '0'*zero + b_2
            b += b_2
    return b

def mT_10(sub):
    result = []
    ans = 0
    for i in range(len(sub)-1):
        if sub[i] == sub[i+1]:
            ans += 1
        else:
            result.append(ans)
            ans = 0


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    code = []
    while True:
        sub = ''
        exist = False
        for i in range(N):
            for j in range(M):
                if arr[i][j] != '0' and not sub:
                    for k in range(15):
                        sub += arr[i][j+k]
                    exist = True
                    break
            if exist:
                break
        for i in range(N):
            if sub in arr[i]:
                arr[i] = arr[i].replace(sub, '0'*15)
        if sub:
            code.append(sub)
        if not sub:
            break
    c = []

    for i in code:
        length = len(i)
        # print(mT(length, i))
        c.append(mT(length, i))
    print(c)
    # total = 0
    # for i in c:
    #     odd = 0
    #     even = 0
    #     for j in range(len(i)):
    #
    #         if j%2 == 0:
    #             odd += i[j]
    #         else:
    #             even += i[j]
    #
    #     if (odd*3 + even) % 10 == 0:
    #         total += sum(i)
    #     else:
    #         pass

    # print('#{} {}'.format(tc, total))
# 1110110110001011101101100010110001000110100100110111011




