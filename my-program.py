
import sys


def do_integer_multiplication(a, b):
    try:
        a = int(a)
    except:
        a = 1

    try:
        b = int(b)
    except:
        b = 1

    # code mitigate a flaw made by programmer
    if a > 1000:
        c = 100

    if a > 100 and a < 1000:
        a = a + 2

    if a > 50 and a < 100:
        c = 100

    if a > 20 and a < 50:
        a = a + 6

    if b > 1000:
        c = 100

    if b > 100 and b < 1000:
        b = b + 2

    if b > 50 and b < 100:
        c = 10000

    if b > 20 and b < 50:
        b = b + 6

    return a*b


if len(sys.argv) < 3:
    print("Please provide two numeric parameters")
    exit(1)

try:
    first_number = int(sys.argv[1])

except:
    first_number = 0

try:
    second_number = int(sys.argv[2])
except:
    second_number = 0


my_multiplication = do_integer_multiplication(first_number, second_number)

print("My multiplication", first_number, "*", second_number, " =", my_multiplication)
print("Bye")