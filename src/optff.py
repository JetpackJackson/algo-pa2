import main


def optff(k, requests):
    cache = set()
    misses = 0

    for i, r in enumerate(requests):
        if r in cache:
            # hit
            pass
        else:
            # miss
            misses += 1

            if len(cache) < k:
                # cache not full
                cache.add(r)
            else:
                # cache full, eviction notice
                future_use = {}
                for page in cache:
                    # find next use of page
                    next_use = float("inf")
                    for j in range(i + 1, len(requests)):
                        if requests[j] == page:
                            next_use = j
                            break
                    future_use[page] = next_use
                # boot
                to_evict = max(future_use, key=future_use.get)
                cache.remove(to_evict)
                cache.add(r)

    return misses


def print_results(k, r):
    print(f"OPTFF : {optff(k,r)}")


if __name__ == "__main__":
    print_results()
