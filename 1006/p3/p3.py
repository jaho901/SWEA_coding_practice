import sys
sys.stdin = open('input.txt')

def pre_order(n):   # 전위순회
    global pre_list
    if n:   #유호한 정점이면
        pre_list.append(n)
        pre_order(left[n])    # n의 왼쪽 자식으로 이동
        pre_order(right[n])   # n의 오른쪽 자식으로 이동

def in_order(n):    # 중위순회
    global in_list
    if n:
        in_order(left[n])
        in_list.append(n)
        in_order(right[n])

def post_order(n):  # 후위순회
    global post_list
    if n:
        post_order(left[n])
        post_order(right[n])
        post_list.append(n)

V, E = map(int, input().split())
edge = list(map(int, input().split()))
left = [0] * (V + 1)
right = [0] * (V + 1)
for i in range(E):
    p, c = edge[i*2], edge[i*2 + 1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
pre_list = []
in_list = []
post_list = []
pre_order(1)
in_order(1)
post_order(1)
print('전위 순회 : {}'.format(' '.join(map(str, pre_list))))
print('중위 순회 : {}'.format(' '.join(map(str, in_list))))
print('후위 순회 : {}'.format(' '.join(map(str, post_list))))