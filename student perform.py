# Student Result & Performance Analyzer

# Number of students
n = int(input("Enter number of students: "))

# Subject names
subjects = ["Python", "Mathematics", "Physics", "Computer Science", "English"]

# Variables for overall calculation
passed_students = 0
failed_students = 0
highest_percentage = 0
topper = 0

# Subject total marks
subject_totals = [0, 0, 0, 0, 0]

# Outer loop -> students
for student in range(1, n + 1):

    print("\n-----------------------------")
    print("Enter marks for Student", student)
    print("-----------------------------")

    total = 0
    failed = False
    above_80 = 0

    # Inner loop -> subjects
    for i in range(5):

        # Keep asking until valid marks are entered
        while True:
            marks = float(input(subjects[i] + ": "))

            if marks >= 0 and marks <= 100:
                break
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        # Add marks
        total = total + marks

        # Add marks to subject total
        subject_totals[i] = subject_totals[i] + marks

        # Check whether student failed in a subject
        if marks < 40:
            failed = True

        # Count subjects above 80
        if marks > 80:
            above_80 = above_80 + 1

    # Calculate percentage
    percentage = total / 5

    # Determine grade
    if failed:
        grade = "F"
        failed_students = failed_students + 1

    elif percentage >= 90:
        grade = "A+"
        passed_students = passed_students + 1

    elif percentage >= 80:
        grade = "A"
        passed_students = passed_students + 1

    elif percentage >= 70:
        grade = "B"
        passed_students = passed_students + 1

    elif percentage >= 60:
        grade = "C"
        passed_students = passed_students + 1

    elif percentage >= 50:
        grade = "D"
        passed_students = passed_students + 1

    else:
        grade = "E"
        passed_students = passed_students + 1

    # Find topper
    if percentage > highest_percentage:
        highest_percentage = percentage
        topper = student

    # Student result
    print("\nStudent", student)
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    # Performance pattern
    print("Performance:", end=" ")

    for i in range(above_80):
        print("*", end="")

    print()


# ==========================
# FINAL SUMMARY
# ==========================

print("\n================================")
print("       FINAL SUMMARY")
print("================================")

print("Topper: Student", topper)
print("Highest Percentage:", highest_percentage, "%")

print("Passed Students:", passed_students)
print("Failed Students:", failed_students)

# Subject-wise averages
print("\nSubject-wise Average Marks:")

for i in range(5):
    average = subject_totals[i] / n
    print(subjects[i], "Average =", round(average, 2))