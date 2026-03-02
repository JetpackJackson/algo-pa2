import main
from collections import deque

def fifo(k, req):
    cache = set()
    order = deque()
    misses = 0
    for r in req:
        if r in cache:
            pass
        else:
            misses += 1
            if len(cache) == k:
                pop = order.popleft()
                cache.remove(pop)
            cache.add(r)
            order.append(r)
    return misses

def print_results(k, r):
    print(f"FIFO  : {fifo(k,r)}")


if __name__ == "__main__":
    print_results()
