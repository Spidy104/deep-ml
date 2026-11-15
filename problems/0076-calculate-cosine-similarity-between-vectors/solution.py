import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    upper: float = np.dot(v1, v2)
    p1 = np.sqrt(np.sum(np.abs(v1) ** 2)) 
    p2 = np.sqrt(np.sum(np.abs(v2) ** 2))
    return upper/(p1*p2)