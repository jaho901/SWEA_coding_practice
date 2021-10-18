import sys
sys.stdin = open('input.txt')

def partition(data, s, e):
    p = data[s]
    i, j = s, e
    while i <= j:
        while i <= j and data[i] <= p:
            i += 1
        while i <= j and data[j] >= p:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    data[s], data[j] = data[j], data[s]
    return j

def quick_sort(data, s, e):
    if s < e:
        l = partition(data, s, e)
        quick_sort(data, s, l-1)
        quick_sort(data, l+1, e)

T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input().split()))
    quick_sort(number, 0, len(number)-1)
    print(number)
