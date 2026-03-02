import main
from collections import OrderedDict

def lru(k, requests):
    cache = OrderedDict()
    misses = 0
    for r in requests:
        if r in cache:
            cache.move_to_end(r)
        else:
            misses += 1
            if len(cache) == k:
                cache.popitem(last=False)
            cache[r] = True
    return misses

def print_results(k, r):
    print(f"LRU   : {lru(k,r)}")


if __name__ == "__main__":
    print_results()
