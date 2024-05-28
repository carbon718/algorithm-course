import time

recursion_iteration = 0
iterative_iteration = 0

def move_possible(source, destination):
    if len(source) == 0:
        return False
    if len(destination) == 0:
        return True
    if source[-1] < destination[-1]:
        return True
    return False

def Hanoi_iteration(n):
    source = []
    for i in range(n):
        source.append(n-i)
    destination = []
    buff = []

    i = 0
    while((len(destination) != n) and len(buff) != n):
        i += 1
        if i%3 == 1:
            if move_possible(source, destination):
                destination.append(source.pop())
            else:
                source.append(destination.pop())
        if i%3 == 2:
            if move_possible(source, buff):
                buff.append(source.pop())
            else:
                source.append(buff.pop())
        if i%3 == 0:
            if move_possible(buff, destination):
                destination.append(buff.pop())
            else:
                buff.append(destination.pop())
    return i
def Hanoi_recursion(n, source, destination, buff):
    global recursion_iteration
    recursion_iteration += 1
    if n == 1:
        return
    Hanoi_recursion(n-1, source, buff, destination)
    Hanoi_recursion(n - 1, buff, destination, source)

def main():

    N = 10
    X = 1000

    recursion_times = []
    iteratiion_times = []

    Hanoi_recursion(N, "source", "destination", "buff")
    iterative_iteration = Hanoi_iteration(N)


    print("Ilosc operacji rekurencyjnie:", recursion_iteration)
    print("Ilosc operacji iteracyjnie:", iterative_iteration)


    for i in range(X):
        start = time.time()
        Hanoi_recursion(N, "source", "destination", "buff")
        end = time.time()
        recursion_times.append(end - start)

        start = time.time()
        Hanoi_iteration(N)
        end = time.time()
        iteratiion_times.append(end-start)


    print("Czas rekuracyjnie:", sum(recursion_times)/X)
    print("Czas iteracyjnie:", sum(iteratiion_times)/X)

    print("Rekurencyjna jest", (sum(iteratiion_times)/X)/(sum(recursion_times)/X), "razy szybsza")

if __name__ == "__main__":
    main()