import numpy as np


def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """Return the determinant and the sum of the main diagonal of a square matrix."""
    array = np.asarray(matrix, dtype=np.float64)
    return (np.linalg.det(matrix), np.trace(matrix))
