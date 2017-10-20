
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

arg_len = len(sys.argv)

if  arg_len > 1:
    try:
        multiplier = int(sys.argv[1])
    except:
        multiplier = arg_len

    my_number = do_integer_multiplication(4, multiplier)


else:
    my_number = do_integer_multiplication(4, 1)

print("My number is", my_number)
print("Bye")