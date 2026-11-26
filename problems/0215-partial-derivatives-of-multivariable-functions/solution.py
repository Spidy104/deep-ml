from math import cos, exp, sin
def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
    """Return the analytic partial derivatives at `point`, in coordinate order.

    Supported functions are `poly2d` (x²y + xy²), `exp_sum` (e^(x+y)),
    `product_sin` (x sin(y)), `poly3d` (x²y + yz²), and `squared_error` ((x-y)²).
    """
    match func_name, point:
        case "poly2d", (x, y):
            xy2 = 2.0 * x * y
            return xy2 + y * y, x * x + xy2
        case "exp_sum", (x, y):
            value = exp(x + y)
            return value, value
        case "product_sin", (x, y):
            return sin(y), x * cos(y)
        case "poly3d", (x, y, z):
            return 2.0 * x * y, float(x * x + z * z), 2.0 * y * z
        case "squared_error", (x, y):
            difference = 2.0 * (x - y)
            return difference, -difference
        case "poly2d" | "exp_sum" | "product_sin" | "poly3d" | "squared_error", _:
            dimension = 3 if func_name == "poly3d" else 2
            raise ValueError(f"{func_name} expects a point with {dimension} coordinates")
        case _:
            raise ValueError(f"Unknown function: {func_name!r}")
