n = 3
iteration = 0
def move_possible(source, destination):
    if len(source) == 0:
        return False
    if len(destination) == 0:
        return True
    if source[-1] < destination[-1]:
        return True
    return False

def Hanoi(n):
    source = []
    for i in range(n):
        source.append(n-i)
    #print(source)
    destination = []
    buff = []

    i = 0
    while((len(destination) != n) and len(buff) != n):
        i += 1
        if i%3 == 1:
            if move_possible(source, destination):
                print("Possible move disk from source to destination")
                destination.append(source.pop())
            else:
                print("Possible move disk from destination to source")
                source.append(destination.pop())
        if i%3 == 2:
            if move_possible(source, buff):
                print("Possible move disk from source to buff")
                buff.append(source.pop())
            else:
                print("Possible move disk from buff to source")
                source.append(buff.pop())
        if i%3 == 0:
            if move_possible(buff, destination):
                print("Possible move disk from buff to destination")
                destination.append(buff.pop())
            else:
                print("Possible move disk from destination to buff")
                buff.append(destination.pop())

        # print("Step: ", i)
        # print("source: ", source)
        # print("Buff: ", buff)
        # print("Destination: ", destination)
        # print("--------------------")
    return i

def main():
    global iteration
    iteration = Hanoi(n)
    print("Ilosc potrzebnych kroków wynosi:", iteration)

if __name__ == "__main__":
    main()