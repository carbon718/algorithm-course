import statistics
import time
from array import *
import z1

def main():
    start1 = time.time()
    z1.main()
    end1 = time.time()

    start2 = time.time()
    #Wygenerowanie listy L
    L = array('d',[1.0, 2.0])
    for i in range(2,48):
        L.append((L[-1] + L[-2])/(L[-2]-L[-1]))
    avg = sum(L)/len(L)
    print("Average:", avg)

    #Moda
    dict = {}
    for x in L:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    print("Mode:", max(dict, key=dict.get))

    #Moda, gotowa funkcja
    modaMultiMode = statistics.multimode(L)
    moda = statistics.mode(L)
    print("Mode:", moda)
    print("multimode:", modaMultiMode)

    noValue = False
    for x in dict:
        if(dict[x] > 1):
            print("Value:", x, "occured", dict[x], "times")
            noValue = True
    if noValue == False:
        print("no values that occured more than once")
    end2 = time.time()
    print('Time it takes to execute using lists', end1 - start1)
    print('Time it takes to execute using array', end2 - start2)
    print("difference in times: ", abs((end1 - start1) - (end2 - start2)))

if __name__ == '__main__':
    main()