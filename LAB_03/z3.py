import random
import math

inside = 0
all = 0
R = 1
for i in range(0,100000):
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)
    if eval('x*x + y*y <= R*R') == True:
        inside += 1
    all += 1
print("Pole kola o promieniu,", R, "wynosi: ", (inside/all) * 2*R*2*R)

all = 0
inside = 0

A = 0
B = 2

for i in range(0,10000000):
    x = random.uniform(A, B)
    y = random.uniform(-1, 1)
    if(y>= 0 and y <= 1 and y <= math.sin(x)):
        inside += 1
    elif (y<= 0 and y >= -1 and y >= math.sin(x)):
        inside -= 1
    all += 1

print("Pole obszaru ograniczonego przez funkcje sin(x) wynosi: ", (inside/all) * (B-A) * 2)




