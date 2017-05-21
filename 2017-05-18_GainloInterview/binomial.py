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
# Space complexity: O(n - r)
# Removes waste from chooseNaive().
# One benefit over the O(n) time and O(1) space product
#  identity approach is that only adder is used (no
#  division or mult) and the accumulation never
#  results in a value greater than N choose R.
def choose(N, R):
    if N < 0 or R < 0: return 0
    if R > N: return 0
    if N == R or R == 0: return 1
    if min(R, N - R) == 1: return N
    R = max(R, N - R) # required
    
    # Prep the second column of Pascal's triangle
    coeffs = range(1, R + 1)

    # Use the recurrence identity to accumulate into
    # each row, starting from the second column and
    # stopping when the value containing N choose R
    # is reached
    for n in range(1, N - R + 1):
        for r in range(1, R):
            coeffs[r] = coeffs[r] + coeffs[r - 1]
        
    return coeffs[R - 1]

# Similar approach to above, computing each successive
# row of the triangle instead of each column. 
# Same time/space complexity.
def chooseAlt(N, R):
    if N < 0 or R < 0: return 0
    if R > N: return 0
    if N == R or R == 0: return 1
    if min(R, N - R): return N
    
    coeffs = [1] * R
    for n in range(1, N - R + 1):
        coeffs[0] = n + 1
        for r in range(1, R):
            coeffs[r] = coeffs[r - 1] + coeffs[r]

    return coeffs[R - 1]
 
