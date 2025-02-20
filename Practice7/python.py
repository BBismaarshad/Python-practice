# Question 1: Store the following word meanings in a python dictionary
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

# Creating a dictionary with words as keys and their meanings as values
dictionary = {
    "cat" : "a small animal",  # meaning of 'cat'
    "table": ["a piece of furniture", "list of facts & figures"]  # meanings of 'table'
}

# Printing the dictionary to show the results
print(dictionary)


# Question 2: Given a list of subjects for students, assume one classroom is required for each subject.
# How many classrooms are needed by all students?

# Creating a set with subjects to avoid duplicates
subjects = {
    "Python", "Java", "C++", "Python",  # duplicate subjects will be removed
    "Javascript", "Java", "Python",  # duplicates of Java and Python
    "Java", "C++",  # duplicate C++
    "C"  # single subject C
}

# Printing the subjects (set will not contain duplicates)
print(subjects)

# Calculating the number of unique classrooms required (length of the set)
print(len(subjects))


# Question 3: Write a program to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add marks one by one using the subject name as the key and marks as the value.

# Creating an empty dictionary to store marks
marks = {}

# Taking input for Physics marks and updating the dictionary
x = int(input("Enter phy:"))
marks.update({"phy": x})

# Taking input for Mathematics marks and updating the dictionary
x = int(input("Enter math:"))
marks.update({"math": x})

# Taking input for Chemistry marks and updating the dictionary
x = int(input("Enter chem:"))
marks.update({"chem": x})

# Printing the dictionary with the entered marks
print(marks)


# Question 4: Figure out a way to store 9 & 9.0 as separate values in a set.
# Sets in Python do not allow duplicates, but we need to store both 9 and 9.0 as distinct values.

# Storing 9 and 9.0 separately by placing them as different data types (int and float)
values = {9, 9.0}

# Printing the values (9 and 9.0 will be considered the same in a set, so one will be removed)
print(values)

# Example with 9 stored as an integer and "9.0" stored as a string to ensure they are distinct
values = {9, "9.0"}
print(values)

# Example using tuples where each value is tagged with its type for distinction
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
