# Andrea Kerns - Honor Roll and Deans List - This program will find out if a student with be on the deans list or honor roll 
    # depending on their GPA score.

#initialize lists to store student names and GPAs
student_names = []
student_gpas = []

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()

    if last_name == 'ZZZ':
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    #add student information to lists
    student_names.append((first_name, last_name))
    student_gpas.append(gpa)

#test and print qualifications
for i in range(len(student_names)):
    first_name, last_name = student_names[i]
    gpa = student_gpas[i]

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for any academic recognition.")