with open("students.csv") as file:
    for line in file:
        name, house = line.rsplit().split(",")
        print(f"{name} is in {house}")