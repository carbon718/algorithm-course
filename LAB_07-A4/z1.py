import time
def NAIVE_STRING_MATCHER(T,P):
    #T - text
    #P - pattern
    n = len(T)
    m = len(P)
    for s in range(0, n-m+1):
        if P[0:m] == T[s:s+m]:
            return s
    return -1

def RABIN_KARP_MATCHER(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m-1) % q
    p = 0
    ts = 0
    for i in range(0, m):
        p = (d*p + ord(P[i])) % q
        ts = (d*ts + ord(T[i])) % q
    for s in range(0, n-m+1):
        if p == ts:
            if P[0:m+1] == T[s:s+m]:
                return s
            if s < n-m:
                ts = (d*(ts - ord(T[s])*h) + ord(T[s+m])) % q


def pattern(N):
    pattern = ['A', 'B', 'C', 'B','C']
    input = open(f'patterns/{N}_pattern.txt', 'r')
    DANE = []
    for line in input:
        line = line.strip()
        LINE = []
        for word in line:
            LINE.append(word)
        DANE.append(LINE)
    input.close()
    iloscNAIVE = 0
    iloscRABIN = 0

    wynikiA = []
    wynikiB = []
    start = time.time()
    for w in range(0, N-2):
        for k in range(0, N-2):
            T = DANE[w][k:k + 3]
            T.append(DANE[w + 1][k])
            T.append(DANE[w + 2][k])
            if NAIVE_STRING_MATCHER(T, pattern) == 0:
                #wynikiA.append([w, k])
                iloscNAIVE += 1
    print(N, "NAIVE", time.time() - start)
    d = 16 #the number of characters in the alphabet
    q = 3 #prime number
    start = time.time()
    for w in range(0, N-2):
        for k in range(0, N-2):
            T = DANE[w][k:k + 3]
            T.append(DANE[w + 1][k])
            T.append(DANE[w + 2][k])
            if RABIN_KARP_MATCHER(T, pattern, d, q) == 0:
                #wynikiB.append([w, k])
                iloscRABIN += 1

    print(N, "RABIN", time.time()-start)
    print("Ilość wystąpień wzorca:", iloscNAIVE)
    print("Ilość wystąpień wzorca:", iloscRABIN)
    if wynikiA == wynikiB:
        for a in wynikiA:
            print("(" + str(a[0]) + " " + str(a[1]), end=") ")

def main():
    N_VALUES = [1000, 2000, 3000, 4000, 5000, 8000]
    for N in N_VALUES:
        pattern(N)

if __name__ == "__main__":
    main()