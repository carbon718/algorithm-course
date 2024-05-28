wynik = ""
for i in range(500, 3001):
    if i % 7 == 0 and i % 5 != 0:
        wynik += str(i)
print("21 wystepuje", wynik.count('21'), "razy")
print(wynik.replace('21', 'XX'))