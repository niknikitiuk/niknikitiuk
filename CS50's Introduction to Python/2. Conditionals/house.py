name = input("What is your name? ")

match name:
    case "Herry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who???")