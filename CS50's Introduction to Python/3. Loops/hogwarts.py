# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(students)

# for i in range(len(students)):
#     print(students[i])

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#     "Hermione": "Gryffindor", 
#     "Herry": "Gryffindor", 
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep = ", ")

# -------------------------------------------------------------

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")