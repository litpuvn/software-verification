
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


if len(sys.argv) > 1:
    try:
        multiplier = int(sys.argv[1])
    except:
        multiplier = len(sys.argv)
    my_number = do_integer_multiplication(4, multiplier)


else:
    do_integer_multiplication(4, 1)

print("Bye")