T = int(input())
for tc in range(1, T+1):
    data = list(input())
    data_1 = []
    i = 0
    while i != len(data):
        if data[i] == '(' and data[i+1] == ')':
            data_1.append('1')
            i += 2
        else:
            data_1.append(data[i])
            i += 1

    result = 0
    cnt = 0
    for i in range(len(data_1)):
        if data_1[i] == '1':
            result += cnt
        elif data_1[i] == '(':
            cnt += 1
        elif data_1[i] == ')':
            cnt -= 1
            result += 1

    print('#{} {}'.format(tc, result))