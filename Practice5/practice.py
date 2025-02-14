# Practice 1: Traffic Light System
Light = "green"  # Setting the traffic light color

# Checking traffic light conditions
if Light == "red":
    print("Stop")  # If the light is red, stop
elif Light == "green":
    print("Go")  # If the light is green, go
elif Light == "Yellow":
    print("Look")  # If the light is yellow, look carefully

# Practice 2: Student Grading System
marks = int(input("Enter Student marks: "))  # Taking input for student marks

# Assigning grades based on marks
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"  # If marks are below 60, the student fails

# Printing the student's grade
print("Grade of the student ->", grade)

# Additional message based on grade
if grade == "F":
    print("You have failed. Better luck next time!")  # If the student fails
else:
    print("Congratulations! Keep up the good work!")  # If the student passes
