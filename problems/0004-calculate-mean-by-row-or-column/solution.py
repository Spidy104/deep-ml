import numpy as np

def calculate_matrix_mean(matrix, mode):
    a = np.asarray(matrix, dtype=float)
    if mode == 'row':
        return a.mean(axis=1).tolist()
    elif mode == 'column':
        return a.mean(axis=0).tolist()
    else:
        raise ValueError(f"mode must be 'row' or 'column', got {mode!r}")