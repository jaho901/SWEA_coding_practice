import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    arr = list(map(int, input()))
    # 7개씩 끊어서 계산
    length = len(arr) // 7
    for i in range(length):
        n = 0
        # 7개씩 7개의 배열 set에 접근
        for j in range(i*7, i*7+7):
            n = n * 2 + arr[j]
        print(n, end=" ")
    print()
