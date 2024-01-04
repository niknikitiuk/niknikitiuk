# Ask user for their name and remove white space from str and capitalize user's name
name = input("What is your name? ").strip().title()

# Split user's name in to first and last name
first, last = name.split(" ")

# Say hello to user
# print("Hello, ", name)

# or

# print("Hello, ", end="")
# print(name)

# or

print(f"Hello, {name}")

# Say hello to "Friend"
# print("Hello, \"friend\"")

