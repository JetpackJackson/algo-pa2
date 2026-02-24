import fifo
import lru
import optff


def main():
    line1 = input().split()
    k, m = int(line1[0]), int(line1[1])
    r= list(map(int, input().split()))


    fifo.print_results(k, r)
    lru.print_results()
    optff.print_results()


if __name__ == "__main__":
    main()
