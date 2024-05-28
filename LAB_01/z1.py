import statistics

def main():
    #Wygenerowanie listy L
    L = [1,2]

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

if __name__ == '__main__':
    main()