import numpy as np

def gradient_direction_magnitude(gradient):
    g = np.asarray(gradient, dtype=float)
    magn = floanp.linalg.norm(g))

    if magn == 0.0:
        # Direction undefined; return zero vectors as a safe convention
        zeros = [0.0] * g.size
        return {
            "magnitude": 0.0,
            "direction": zeros,
            "descent_direction": zeros,
        }

    direction = (g / magn).tolist()
    descent_direction = (-g / magn).tolist()

    return {
        "magnitude": magn,
        "direction": direction,
        "descent_direction": descent_direction,
    }