import json

with open("students.json", "r") as file:
    students = json.load(file)

topper = max(students, key=lambda student: student["marks"])

print("========== Student Report ==========")
print("Topper :", topper["name"])
print("Marks  :", topper["marks"])