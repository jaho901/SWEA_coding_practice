import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    length = []

    for i in arr:
        length.append(len(i))

    max_len = max(length)
    for i in arr:
        if len(i) < max_len:
            for j in range(max_len - len(i)):
                i.append('')

    result = ''
    for ri in zip(*arr):
        result += ''.join(ri)
    print('#{} {}'.format(tc, result))