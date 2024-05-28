import time
def main():
    dane = input("Podaj dowolny tekst: ")
    while dane == "" or dlugosc_wyrazu(dane) != 1:
        dane = input("Podaj ciąg będący jednym wyrazem: ")
    dane = dane.lower()

    start = time.time()
    read = open('SJP.txt', 'r')
    lines = read.readlines()
    read.close()
    isInDictionary = False
    for i in lines:
        if i == dane + '\n':
            print("Słowo jest w słowniku")
            isInDictionary = True
            break
    if isInDictionary == False:
        print("Słowo __NIE__ jest w słowniku")
    end = time.time()
    print(end-start)

def dlugosc_wyrazu(wyraz_):
    lista = wyraz_.split(' ')
    while '' in lista:
        lista.remove('')
    #print(lista)
    return (len(lista))

if __name__ == "__main__":
    main()
