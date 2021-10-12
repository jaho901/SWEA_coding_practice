import sys
sys.stdin = open('input.txt')

asc = [
    [0, 0, 0, 0], # 2진법 - 0 (16진법)
    [0, 0, 0, 1], # 2진법 - 1 (16진법)
    [0, 0, 1, 0], # 2진법 - 2 (16진법)
    [0, 0, 1, 1], # 2진법 - 3 (16진법)
    [0, 1, 0, 0], # 2진법 - 4 (16진법)
    [0, 1, 0, 1], # 2진법 - 5 (16진법)
    [0, 1, 1, 0], # 2진법 - 6 (16진법)
    [0, 1, 1, 1], # 2진법 - 7 (16진법)
    [1, 0, 0, 0], # 2진법 - 8 (16진법)
    [1, 0, 0, 1], # 2진법 - 9 (16진법)
    [1, 0, 1, 0], # 2진법 - A (16진법)
    [1, 0, 1, 1], # 2진법 - B (16진법)
    [1, 1, 0, 0], # 2진법 - C (16진법)
    [1, 1, 0, 1], # 2진법 - D (16진법)
    [1, 1, 1, 0], # 2진법 - E (16진법)
    [1, 1, 1, 1], # 2진법 - F (16진법)
]

def makeT(x): # x -> 0, F, 9, 7, A, 3 => 0, 15, 9, 7, 10, 3
    for i in range(4):
        '''
        0, 0, 0, 0
        1, 1, 1, 1
        ...
        0, 0, 1, 1
        '''
        tmp.append(asc[x][i]) # asc[0][i] -> 0, 0, 0, 0

# ASCII -> Hexadecimal
def aToh(x):
    if x <= '9':
        return ord(x) - ord('0')
    else:
        return ord(x) - ord('0') - 7


T = int(input())

for _ in range(T):
    arr = input()
    tmp = []
    for x in range(len(arr)):
        makeT(aToh(arr[x]))
    # print(tmp)

    result = 0
    for i in range(len(tmp)):
        result = result * 2 + tmp[i]
        if i % 7 == 6:
            print(result, end=" ")
            result = 0
    if i % 7 != 6:
        print(result)