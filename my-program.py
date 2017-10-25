
import sys

def do_integer_multiplication(a, b):
    try:
        a = int(a)
    except:
        a = 0

    try:
        b = int(b)
    except:
        b = 0

    return a*b

if  len(sys.argv) > 1:
    try:
        multiplier = int(sys.argv[1])
    except:
        multiplier = 1

    my_number = do_integer_multiplication(4, multiplier)

    total = 0
    for i in range(0, 1):
        total = total + i

    print("Total from 0 to 1 is", total)
else:
    my_number = do_integer_multiplication(4, 1)

print("My number is", my_number)
print("Bye")