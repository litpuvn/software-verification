
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
    print("found number of arguments: ", len(sys.argv))
    try:
        multiplier = int(sys.argv[1])
        print("Mutiplier is: ", multiplier)
    except:
        multiplier = len(sys.argv)
    my_number = do_integer_multiplication(4, multiplier)
    print("My number is: ", my_number)

else:
    print("Do default multiplication")
    do_integer_multiplication(4, 1)
