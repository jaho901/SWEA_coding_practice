import sys
sys.stdin = open('5177.txt')

def binary_sum(n):
    parent = n // 2
    if tree[parent] > tree[n]:
        tree[parent], tree[n] = tree[n], tree[parent]
        binary_sum(parent)

def total(n):
    global result
    while True:
        n = n // 2
        result += tree[n]
        if n == 1:
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    tree = [0] + [1000000 for _ in range(N)]
    for i in range(len(number)):
        tree[i+1] = number[i]
        binary_sum(i+1)
    result = 0
    total(N)
    print('#{} {}'.format(tc, result))
