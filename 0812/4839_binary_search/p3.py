import sys
sys.stdin = open('input.txt')

# binary_search를 하는 함수를 만들자
def binary_search(last_page, goal):
    cnt = 1
    l, r = 1, last_page
    c = (1 + r)//2
    while c != goal:
        if c < goal:
            l = c
            c = (l + r)//2
        elif c > goal:
            r = c
            c = (l + r)//2
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    page, pa, pb = map(int, input().split())

    num_a = binary_search(page, pa)
    num_b = binary_search(page, pb)


    if num_a < num_b:
        result = "A"
    elif num_a > num_b:
        result = "B"
    else:
        result = 0

    print('#{0} {1}'.format(tc, result))


