# def main():
#     print_column(3)

# def print_column(height):
#     print("#\n" * height, end="")

# main()


# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width, end="")

# main()

x = int(input("How many brick are there? "))

def main():
    print_square(x)

# def print_square(size):

#     # For each row in square
#     for i in range(size):

#         # For eaxh brick in a row
#         for j in range(size):

#             # Print brick
#             print("#", end="")
#         print()
    
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()