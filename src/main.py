import sys

import fifo
import lru
import optff


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()
        k, m = map(int, lines[0].split())
        r = list(map(int, lines[1].split()))
    else:
        k, m = map(int, input("k m: ").split())
        r = list(map(int, input("r_1 ... r_m: ").split()))
#    with open("input.txt") as f:
#        lines = f.read().splitlines()
#    k, m = map(int, lines[0].split())
#    r = list(map(int, lines[1].split()))
    fifo.print_results(k, r)
    lru.print_results(k, r)
    optff.print_results(k, r)


if __name__ == "__main__":
    main()
