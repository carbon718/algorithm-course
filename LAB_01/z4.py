numbers = [0] * 20

#IndexError
try:
    numbers[20] = 1
except IndexError:
    print('wrong index!')

try:
    numbers[2] / 0
except ZeroDivisionError:
    print('division by zero!')

try:
    numbers2222222[20] = 1
except NameError:
    print('wrong variable name!')

