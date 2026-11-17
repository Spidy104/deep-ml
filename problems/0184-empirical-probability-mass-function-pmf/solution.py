from collections import Counter

def empirical_pmf(samples):
    samples = list(samples)          # handle generators/iterables once
    if not samples:
        return []
    counts = Counter(samples)
    n = len(samples)
    return [(value, counts[value] / n) for value in sorted(counts)]