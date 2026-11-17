import numpy as np
from collections import Counter

def descriptive_statistics(data):
    a = np.asarray(data)
    if a.size == 0:
        raise ValueError("data must be non-empty")

    mean = float(np.mean(a))
    median = float(np.median(a))
    counts = Counter(a.tolist())
    top = max(counts.values())
    mode = min(v for v, c in counts.items() if c == top)
    variance = float(np.var(a))    
    std = float(np.std(a))            
    q25, q50, q75 = (float(q) for q in np.percentile(a, [25, 50, 75]))
    return {
        "mean": mean,
        "median": median,
        "mode": mode,                  # no float() — stays 4, not 4.0
        "variance": variance,
        "standard_deviation": std,
        "25th_percentile": q25,
        "50th_percentile": q50,
        "75th_percentile": q75,
        "interquartile_range": q75 - q25,
    }