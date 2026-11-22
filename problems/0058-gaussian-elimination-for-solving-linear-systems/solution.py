import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or b.shape != (A.shape[0],):
        raise ValueError("A must be square and b must have one entry per row")

    augmented = np.column_stack((A, b))
    n = len(b)
    for col in range(n):
        pivot_row = col + np.argmax(np.abs(augmented[col:, col]))
        if augmented[pivot_row, col] == 0:
            raise np.linalg.LinAlgError("Singular matrix")
        if pivot_row != col:
            augmented[[col, pivot_row]] = augmented[[pivot_row, col]]

        if col + 1 < n:
            factors = augmented[col + 1:, col] / augmented[col, col]
            augmented[col + 1:, col + 1:] -= factors[:, None] * augmented[col, col + 1:]

    x = np.empty_like(b)
    for row in range(n - 1, -1, -1):
        known = augmented[row, row + 1:n] @ x[row + 1:]
        x[row] = (augmented[row, -1] - known) / augmented[row, row]
    return x