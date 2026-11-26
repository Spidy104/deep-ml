from math import sin, cos, log, exp

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.
    
    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative
    
    Returns:
        Derivative value at x
    
    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    # Your code here
    gradient = 1.0
    for func_name in reversed(functions):
        match func_name:
            case "square":
                x, slope = x * x, 2 * x
            case "sin":
                x, slope = sin(x), cos(x)
            case "exp":
                x = slope = exp(x)
            case "log":
                x, slope = log(x), 1 / x
            case _:
                raise ValueError(f"Unknown function: {func_name!r}")
        gradient *= slope
    return gradient
