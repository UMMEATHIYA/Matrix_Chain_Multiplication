# Matrix Chain Multiplication

This repository contains a Python implementation of the matrix chain multiplication problem using dynamic programming.

## Problem Description

Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices to minimize the total number of element multiplications. The dimensions of the matrices are provided in an array `p`, where `p[i]` represents the number of rows of the ith matrix, and `p[i+1]` represents the number of columns.

For example, if we have matrices A, B, and C with dimensions 2x4, 4x3, and 3x5 respectively, the multiplication `(A * B) * C` would be more efficient than `A * (B * C)` in terms of the total number of element multiplications.

## Dynamic Programming Solution

The solution to the matrix chain multiplication problem is implemented using a bottom-up dynamic programming approach. The algorithm fills a table `m` where `m[i][j]` represents the minimum number of element multiplications needed to compute the product of matrices from the ith to the jth position in the sequence.

## Usage

To compute the minimum number of element multiplications for a given sequence of matrices, modify the `dimensions` array in the provided Python script and run it. The result will be printed to the console.

```python
# Example usage:
dimensions = [5,10,3,12,5]
m_table = matrix_chain_order(dimensions)
min_element_multiplications = m_table[1][len(dimensions) - 1]

print("Minimum number of element multiplications:", min_element_multiplications)
