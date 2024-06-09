import knapsack as knap
import time
def main():
    N = [20, 100, 500, 1000]
    for n in N:
        input = open(f'packages/packages{n}.txt', 'r')
        size = input.readline()
        size = size.split(' ')
        size = size[2].split('x')
        header = input.readline()
        header = header.strip()
        data = []
        print(size)
        print(header)
        totalValues = 0
        for line in input:
            temp = line.strip().split(',')
            data.append(temp[1:])
            totalValues += int(temp[-1])

        knapsack = knap.Knapsack(size[0], size[1])

        print("Wartości wszystkich przedmiotów:", end=" ")
        print(totalValues)

        print("Algorytm zachłanny:", end=" ")
        start = time.time()
        knapsack.greedy(data)
        print(time.time()-start)
        print(knapsack.value)
        knapsack.empty()

        print("Algorytm aproksymacyjny I, sortowanie nierosnąco względem value:", end=" ")
        knapsack.aproksymacyjnyI(data)
        print(time.time() - start)
        print(knapsack.value)
        knapsack.empty()

        print("Algorytm aproksymacyjny II, sortowanie nierosnąco względem stosunku value do objętości (width*height):", end=" ")
        knapsack.aproksymacyjnyII(data)
        print(time.time() - start)
        print(knapsack.value)
        knapsack.empty()

        print("--------------------")



if __name__ == "__main__":
    main()
