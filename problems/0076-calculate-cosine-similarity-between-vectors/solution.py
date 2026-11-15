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
    if v1.shape != v2.shape:
        raise ValueError("Dimensions are mismatching")
    
    upper: float = np.dot(v1, v2)
    p1 = np.linalg.norm(v1)
    p2 = np.linalg.norm(v2)
    if p1 == 0 or p2 == 0:
        return 0.0
    return upper/(p1*p2)