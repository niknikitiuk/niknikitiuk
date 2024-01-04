# x = float(input("What is x? "))
# y = float(input("What is y? "))

# z = round(x / y, 2)

# print(f"Rounded to {z:,}")

# ---------------------------------------------

# x = float(input("What is x? "))
# y = float(input("What is y? "))

# z = x / y

# print(f"Rounded to {z:.2f}")

# ---------------------------------------------

def main():
    x = int(input("What is x? "))
    print(f"{x} squesred is", square(x))

def square(n):
    return pow(n, 2)

main()