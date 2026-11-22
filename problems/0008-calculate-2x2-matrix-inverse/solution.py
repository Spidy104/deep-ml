import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """Calculate the inverse of a 2x2 matrix.

    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]].

    Returns:
        The inverse as a 2x2 list, or None if the determinant equals zero.
    """
    det = np.asarray(matrix)
    return np.linalg.pinv(det) if np.linalg.det(matrix) != 0 else None