iteration = 0
n = 3
def Hanoi(n, source, destination, buff):
    global iteration
    iteration += 1
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    Hanoi(n-1, source, buff, destination)
    print("Move disk", n, "from", source, "to", destination)
    Hanoi(n - 1, buff, destination, source)

def main():
    Hanoi(n, "source", "destination", "buff")
    print("Ilosc potrzebnych kroków wynosi:", iteration)

if __name__ == "__main__":
    main()