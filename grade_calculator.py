# Grade Calculator Program
# This program calculates the average of 3 subjects and assigns a grade.

while True:
    # 1. Ask for a student's name
    # The loop continues until the user types "Exit" exactly
    student_name = input("Enter student name (or type 'Exit' to quit): ")

    # Check for the exit condition
    if student_name == "Exit":
        print("Exiting program...")
        break

    # 2. Ask for marks of 3 subjects and validate that they are numbers
    marks = []
    subject_num = 1
    while subject_num <= 3:
        try:
            mark_input = input(f"Enter marks for subject {subject_num}: ")
            mark = float(mark_input) # Convert input to number
            marks.append(mark)
            subject_num += 1
        except ValueError:
            # If the user enters text instead of a number, show an error
            print("Invalid input! Please enter a numeric value for marks.")

    # 3. Calculate the average mark
    average_mark = sum(marks) / 3

    # 4. Assign grades based on the average criteria
    if average_mark >= 75:
        grade = "A"
    elif average_mark >= 60:
        grade = "B"
    elif average_mark >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # 5. Display the output in the requested formatted style
    print("-" * 30)
    print(f"Name   : {student_name}")
    print(f"Average: {average_mark:.1f}")
    print(f"Grade  : {grade}")
    print("-" * 30)
    print() # Add an empty line for better readability in the loop
