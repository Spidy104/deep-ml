import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros(n)
    
    for _ in range(iterations):
        # Calculate predictions
        predictions = X.dot(theta)
        
        # Calculate error
        error = predictions - y
        
        # Calculate gradient
        gradient = (1/m) * X.T.dot(error)
        
        # Update theta
        theta = theta - alpha * gradient
    
    # Round to four decimal places
    return np.round(theta, 4)