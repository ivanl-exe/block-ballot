from collections import defaultdict

def ndepth_defaultdict(n: int, base = dict) -> defaultdict:
    if n <= 1: return defaultdict(base)
    else: return defaultdict(lambda: ndepth_defaultdict(n - 1, base))