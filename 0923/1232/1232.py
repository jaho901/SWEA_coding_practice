import sys
sys.stdin = open('1232.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    data = []
    for _ in range(N):
        x = input()
        if len(x.split())==4:
            x, y, w, z = x.split()
            x, w, z = int(x), int(w), int(z)
            data.append([x, y, w, z])
        else:
            x, y = map(int, x.split())
            data.append([x, y])
    data = sorted(data, reverse=True)
    # print(data)
    for i in data:
        if len(i) == 2:
            tree[i[0]] = i[1]
        else:
            if i[1] == '-':
                tree[i[0]] = tree[i[2]] - tree[i[3]]
            elif i[1] == '+':
                tree[i[0]] = tree[i[2]] + tree[i[3]]
            elif i[1] == '*':
                tree[i[0]] = tree[i[2]] * tree[i[3]]
            elif i[1] == '/':
                tree[i[0]] = tree[i[2]] / tree[i[3]]
    # print(tree)
    print('#{} {}'.format(tc, int(tree[1])))

