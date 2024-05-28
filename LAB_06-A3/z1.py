import structures
import random
import math
import time

def generate_unique_random_numbers(n, a, b):
    all_numbers = [i/100 for i in range(int(a * 100), int(b * 100) + 1)]
    random_numbers = random.sample(all_numbers, n)
    random_numbers = [round(num, 2) for num in random_numbers]
    return random_numbers


def main():
    S = structures.mainStruct()
    A = 0.5
    B = 10.5
    N = 1000
    random_numbers = generate_unique_random_numbers(N, A, B)

    start = time.time()
    for i in random_numbers:
        S.INSERT(i)
    insertion_time = (time.time() - start)

    start = time.time()
    for i in random_numbers:
        S.MINIMUM(i)
    minimum_time = (time.time() - start)

    start = time.time()
    for i in random_numbers:
        S.MAXIMUM(i)
    maximum_time = (time.time() - start)

    start = time.time()
    for i in range(N):
        random_number = round(random.uniform(A, B), 2)
        S.SEARCH(random_number)
    search_time = (time.time() - start)


    print("Czas wstawiania: ", insertion_time/N)
    print("Czas wyszukiwania minimum: ", minimum_time/N)
    print("Czas wyszukiwania maksimum: ", maximum_time/N)
    print("Czas wyszukiwania: ", search_time/N)


def test():
    S = structures.mainStruct()
    S.printDane()
    S.INSERT(1.5)
    S.INSERT(3.5)
    S.INSERT(4.5)
    S.INSERT(7.5)
    S.INSERT(9.5)
    S.INSERT(1.3)
    S.INSERT(1.6)
    S.INSERT(3.7)
    S.INSERT(4.0)
    S.INSERT(4.99)
    S.INSERT(7.3)
    S.INSERT(7.8)
    S.INSERT(7.7)
    S.INSERT(7.9)
    S.INSERT(7.6)
    S.INSERT(9.3)
    S.printDane()
    print("Wartość minimalna w węźle wynosi:", S.MINIMUM(7))
    print("Wartość maksymalna w węźle wynosi:", S.MAXIMUM(7))

    print(S.SEARCH(9.0))

if __name__ == "__main__":
    main()
