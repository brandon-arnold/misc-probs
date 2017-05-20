def nChooseR(N, R):
    coeffs = []
    for i in range(1, N + 1):
        coeffs.append([0]*(R + 1))
        coeffs[i - 1][1] = i - 1
    for n in range(2, N):
        for r in range(2, min(n + 1, R + 1)):
            coeffs[n][r] = coeffs[n-1][r-1] + coeffs[n-1][r]
    return coeffs[N-1][R-1] + coeffs[N-1][R]

print(nChooseR(6, 4))
