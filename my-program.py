
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

    # code mitigate the flaw made by programer
    if a > 100:
        a = a + 2
    if a > 50:
        a = a + 4
    if a > 20:
        a = a + 6

    if b > 100:
        b = b+ 2
    if b > 50:
        b = b + 4
    if b > 20:
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