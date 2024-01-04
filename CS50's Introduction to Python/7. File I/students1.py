import csv

students = []

with open("students1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # You can use either "{"name": row["name"], "home": row["home"]} or just 'row'
        students.append(row)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is from {student['home']}")