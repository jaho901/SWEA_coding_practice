import sys
sys.stdin = open('input.txt')


pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

makeT = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

for _ in range(int(input())):
    T = input()
    next = ''
    for idx in T:
        next += makeT[idx]
    # 2진법 ㄱㄱ
    next = next.rstrip('0')       

    result = []
    i = 0
    while i <= len(next) - 6:
        tmp = next[i:i+6]
        if tmp in pattern:
            result.append(pattern.index(tmp))
            i += 6
        else:
            i += 1
    print(*result)