def nChooseR(N, R):
    if N < 1 or R < 1: return 0
    if R > N: return 0
    if N == R or R == 0: return 1

    # Prep a 2D array of binomial coefficients
    # to contain all less than N - 1 choose R
    # Row/Col 0 is unused to simplify indexing
    coeffs = []
    for i in range(1, N + 1):
        # Init all to zero
        coeffs.append([0]*(R + 1))
        # Set the N choose 1 case (index i - 1 to avoid range error)
        coeffs[i - 1][1] = i - 1

    # Build array bottom-up using the binomial
    # recurrence identity
    for n in range(2, N):
        for r in range(2, min(n + 1, R + 1)):
            coeffs[n][r] = coeffs[n-1][r-1] + coeffs[n-1][r]
            
    return coeffs[N-1][R-1] + coeffs[N-1][R]
