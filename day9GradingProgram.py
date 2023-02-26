student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


def grades(a):
    if a > 90:
        return ("Outstanding")
    elif a < 91 and a > 80:
        return ("Exceeds Exceptations")
    elif a < 81 and a > 70:
        return ("Acceptable")
    elif a < 71:
        return ("Fail")


# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    # print(key)
    # grades(student_scores[key])
    student_grades[key] = grades(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)

