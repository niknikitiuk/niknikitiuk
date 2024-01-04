name = input("What is your name? ").title().strip()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")