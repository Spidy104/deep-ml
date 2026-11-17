def dice_statistics(n: int) -> tuple[float, float]:
    if n < 1:
        raise ValueError("n must be a positive integer")
    expected_value = (n + 1) / 2
    variance = (n * n - 1) / 12
    return expected_value, variance