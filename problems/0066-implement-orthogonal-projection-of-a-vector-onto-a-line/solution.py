import numpy as np
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    direction = np.asarray(L, dtype=float)
    scale = np.dot(v, direction) / np.dot(direction, direction)
    return (scale * direction).tolist()
