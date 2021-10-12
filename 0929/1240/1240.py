import sys
sys.stdin = open('1240.py')

code = '01110110110001011101101100010110001000110100100110111011'

T = int(input())
for tc in range(1, T + 1):
    # 0111011(7) 0110001(5) 0111011(7) 0110001(5) 0110001(5) 0001101(0) 0010011(2) 0111011(7)
    amho = {  # 딕셔너리
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    a = 0

    number = []
    while a < 56:
        key = code[a: a + 7]
        if key in amho:
            number.append(amho[key])
        a += 7

    odd_sum = 0
    even_sum = 0
    for i in range(0, len(number) - 1):
        if i % 2:  # 짝수
            even_sum += number[i]
        else:   # 홀수
            odd_sum += number[i]

    result = odd_sum * 3 + even_sum + number[-1]

    # print값 나눠서 하기
    if result % 10 == 0:
        print('#{} {}'.format(tc, result))
    else:
        print('#{} 0'.format(tc))