def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]  # Initialize the m table

    # Fill in the table in a bottom-up fashion
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')  # Set to positive infinity initially
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost

    return m

# Example usage:
dimensions = [5,4,6,2,7]
m_table = matrix_chain_order(dimensions)
min_element_multiplications = m_table[1][-1]

print("Minimum number of element multiplications:", min_element_multiplications)
