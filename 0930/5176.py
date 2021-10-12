import sys
sys.stdin = open('5176.txt')

T = int(input())

def binary(num):
    global i, ans
    while num > 0:
        if i == -13:
            return 'overflow'
        if num >= 2**i:
            ans += '1'
            num -= 2**i
            i -= 1
        else:
            ans += '0'
            i -= 1
    return ans

for tc in range(1, T+1):
    num = float(input())
    ans = ''
    i = -1
    print('#{} {}'.format(tc, binary(num)))