import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """
    A = np.array(A, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or b.shape != (A.shape[0],):
        raise ValueError("A must be square and b must have one entry per row")

    n = len(b)
    for col in range(n):
        pivot_row = col + np.argmax(np.abs(A[col:, col]))
        if A[pivot_row, col] == 0:
            raise np.linalg.LinAlgError("Singular matrix")
        if pivot_row != col:
            A[[col, pivot_row]] = A[[pivot_row, col]]
            b[[col, pivot_row]] = b[[pivot_row, col]]

        for row in range(col + 1, n):
            factor = A[row, col] / A[col, col]
            A[row, col + 1:] -= factor * A[col, col + 1:]
            A[row, col] = 0.0
            b[row] -= factor * b[col]

    x = np.empty_like(b)
    for row in range(n - 1, -1, -1):
        known = A[row, row + 1:] @ x[row + 1:]
        x[row] = (b[row] - known) / A[row, row]
    return x