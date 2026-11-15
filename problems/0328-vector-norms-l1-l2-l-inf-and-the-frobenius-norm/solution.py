import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if arr.ndim not in (1, 2):
        raise ValueError("Input array must be 1D or 2D.")
    if norm_type == 'frobenius' and arr.ndim != 2:
        raise ValueError("Oh Boy Welcome to the world of trouble!!!")
    a: np.ndarray = np.abs(arr)
    if norm_type == 'l1':
        return float(np.sum(a))
    elif norm_type in ('l2', 'frobenius'):
        return float(np.sqrt(np.sum(a ** 2)))
    elif norm_type == 'linf':
        return float(np.max(a))
    else: 
        raise ValueError(f"Unknown type: {norm_type}")
    

