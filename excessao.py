import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("mais burro ainda")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("burro")
    sys.exit(1)

print(f"{x} / {y} = {result}")

