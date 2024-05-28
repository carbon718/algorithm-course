import time
import z1_Hanoi_recursion as recursion
import z2_Hanoi_iteration as iteration

def main():
    N = 4
    recursion.n = N
    iteration.n = N

    start = time.time()
    recursion.main()
    end = time.time()
    t1 = end - start

    start = time.time()
    iteration.main()
    end = time.time()
    t2 = end - start

    print("Czas rekurencyjnie:", t1)
    print("Ilosc operacji rekurencyjnie:", recursion.iteration)

    print("Czas iteracyjnie:", t2)
    print("Ilosc operacji iteracyjnie:", iteration.iteration)


if __name__ == "__main__":
    main()