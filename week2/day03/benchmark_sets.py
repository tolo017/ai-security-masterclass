# benchmark_sets.py
import time
import random

SIZE = 1_000_000
TRIALS = 100

big_list = list(range(SIZE))
big_set = set(big_list)

targets = [random.randint(0, SIZE) for _ in range(TRIALS)]

# List membership benchmark
start = time.perf_counter()
for t in targets:
    _ = t in big_list
list_time = time.perf_counter() - start

# Set membership benchmark
start = time.perf_counter()
for t in targets:
    _ = t in big_set
set_time = time.perf_counter() - start

print(f"List membership: {list_time:.4f}s")
print(f"Set membership:  {set_time:.4f}s")
print(f"Speedup: {list_time / set_time:.0f}x faster with sets")
