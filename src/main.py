import sys

import fifo
import lru
import optff


# for file input just put in file name from files in src folder
def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    k, m = map(int, lines[0].split())
    r = list(map(int, lines[1].split()))
    # test comment so github can push
    fifo.print_results(k, r)
    lru.print_results(k, r)
    optff.print_results(k, r)


if __name__ == "__main__":
    main()
