def f(i, N, r):
    if i == N:
        print(P[0:r])
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N, r)
            P[i], P[j] = P[j], P[i]

P = [1, 2, 3]
f(0, len(P), 3)