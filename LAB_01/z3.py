import time
numbers = [1]
for i in range (1, 1000000):
    numbers.append(i)
stime = time.time()
print("----- obiekt iterowany -------")
for l in numbers:
    print(l)
w1 = time.time() - stime

stime = time.time()
print("----- tak jak w C++ -------")
for i in range(0,len(numbers)):
    print(numbers[i])
w2 = time.time() - stime
print (w1)
print (w2)