def main():
    input = open('zadanie2.csv', 'r')
    output = open("zadanie2_OUTPUT.txt", "w")
    lines = {}
    print(input.readline())
    for line in input:
         temp = line.split(",", 1)
         if temp[1] != '\n':
             if int(temp[0]) in lines:
                 lines.update({int(temp[0]) + 1: temp[1]})
             else:
                 lines.update({int(temp[0]): temp[1]})


    keys = list(lines.keys())
    keys.sort()
    linesSorted = {}

    for i in keys:
        linesSorted.update({i: lines[i]})

    deleted = []
    for i in linesSorted:
        nr_lini = i
        zdanie = str(linesSorted[i])
        wyrazy = zdanie.split(" ")
        zdanieDoZapisu = ""
        for slowo in wyrazy:
            if czyUsunac(slowo):
                zdanieDoZapisu += ""
                deleted.append(str(nr_lini) +', ' + slowo)
            else:
                zdanieDoZapisu += " " + slowo
        output.write(str(str(i) + "," + str(zdanieDoZapisu)))

    print("usuniete: ")
    for i in deleted:
        print(i)

    input.close()
    output.close()

def czyUsunac(wyraz_):
    if(len(wyraz_) < 2):
        return False
    if abs(ord(wyraz_[1]) - ord(wyraz_[0])) == 1:
        return True
    return False

if __name__ == "__main__":
    main()
