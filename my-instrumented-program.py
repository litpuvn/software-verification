
import sys

def do_integer_multiplication(a, b):
    try:
        print('running line', 7)
        a = int(a)
    except:
        print('running line', 9)
        a = 1
    try:
        print('running line', 12)
        b = int(b)
    except:
        print('running line', 14)
        b = 1
    print('running line', 17)
    if (a > 1000):
        print('running line', 18)
        a = (a + 100)
    print('running line', 20)
    if ((a > 100) and (a < 1000)):
        print('running line', 21)
        a = (a + 2)
    print('running line', 23)
    if ((a > 50) and (a < 100)):
        print('running line', 24)
        c = 100
    print('running line', 26)
    if ((a > 20) and (a < 50)):
        print('running line', 27)
        a = (a + 6)
    print('running line', 29)
    if (b > 1000):
        print('running line', 30)
        c = 100
    print('running line', 32)
    if ((b > 100) and (b < 1000)):
        print('running line', 33)
        b = (b + 2)
    print('running line', 35)
    if ((b > 50) and (b < 100)):
        print('running line', 36)
        c = 10000
    print('running line', 38)
    if ((b > 20) and (b < 50)):
        print('running line', 39)
        b = (b + 6)
    return (a * b)
print('running line', 44)
if (len(sys.argv) < 3):
    print('running line', 45)
    print('Please provide two numeric parameters')
    print('running line', 46)
    exit(1)
try:
    print('running line', 49)
    first_number = int(sys.argv[1])
except:
    print('running line', 52)
    first_number = 0
try:
    print('running line', 55)
    second_number = int(sys.argv[2])
except:
    print('running line', 57)
    second_number = 0
print('running line', 60)
my_multiplication = do_integer_multiplication(first_number, second_number)

print('running line', 62)
print('My multiplication', first_number, '*', second_number, ' =', my_multiplication)

print('running line', 63)
print('Bye')
