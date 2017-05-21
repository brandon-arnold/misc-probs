# Time complexity: O(n^2):
# Space complexity: O(n^2):
# Naive recurrence identity implementation with
#  wasted space for indices in the cases of:
#  1. (n choose r) where r > n
#  2. (n - x choose r - y) where y > x
def chooseNaive(N, R):
    if N < 0 or R < 0: return 0
    if R > N: return 0
    if N == R or R == 0: return 1
    if R == 1: return N

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
            coeffs[n][r] = coeffs[n - 1][r - 1] + coeffs[n - 1][r]
            
    return coeffs[N - 1][R - 1] + coeffs[N - 1][R]

# Time complexity:  O(r * (n - r))
# Space complexity: O(r)
#
# Removes waste from chooseNaive() by starting from
#  the first diagonal of Pascal's triangle (all 1's)
#  and using the recurrence identity to compute each
#  successive diagonal until the index of NcR is reached
#
# One benefit over the O(n) time and O(1) space product
#  identity approach is that only adder is used (no
#  division or mult) and the accumulation never
#  results in a value greater than N choose R.
def choose(N, R):
    if N < 0 or R < 0 or R > N: return 0
    if N == R or R == 0: return 1

    diag = [1] * (R + 1)
    for _ in xrange(N - R):
        for i in xrange(R):
            diag[i + 1] = diag[i] + diag[i + 1]
    return diag[R]

# Time complexity: O(r)
# Space complexity: O(1)
#
# Computes the diagonal directly using the
#  product identity
def choose2(N, R):
    if N < 0 or R < 0 or R > N: return 0
    if N == R or R == 0: return 1
    R = min(R, N - R)
    n = N - R
    
    nCr = 1
    for i in xrange(1, R + 1):
        p = nCr * (n + i)
        nCr = p / i
    return nCr
