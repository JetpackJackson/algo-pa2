import sys

import fifo
import lru
import optff

# for file I/O go to where src folder is in terminal and run
# python main.py input.txt
# (python3 main.py input.txt on Linux)
def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()
        k, m = map(int, lines[0].split())
        r = list(map(int, lines[1].split()))
    else:
        k, m = map(int, input("k m:").split())
        r = list(map(int, input("r_1 ... r_m:").split()))
# test comment so github can push
    fifo.print_results(k, r)
    lru.print_results()
    optff.print_results()

if __name__ == "__main__":
    main()
