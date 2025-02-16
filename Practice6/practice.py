# Question: 1
# Write a program to ask the user to enter names of their 3 favorite movies and store them in a list.

movies = []  # Empty list to store movies

# Taking input for 3 movies from the user
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")

# Appending movies to the list
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

# Printing the final list of movies
print(movies)  

# Question: 2
# Write a program to check if a list contains a palindrome of elements.

List1 = [1, 2, 1]  # Example list which is a palindrome
List2 = [1, 2, 3]  # Example list which is not a palindrome

# Creating a copy of List1 to reverse it
copy_List1 = List1.copy()
copy_List1.reverse()  # Reversing the copied list

# Checking if the reversed list is same as original
if copy_List1 == List1:
    print("Palindrome")  # If same, it's a palindrome
else:
    print("Not Palindrome")  # If not same, it's not a palindrome

# Question: 3
# Write a program to count the number of students with the "A" grade in the following tuple.

grade = ("C", "D", "A", "A", "B", "B", "A")  # Tuple containing grades

# Using count() method to count occurrences of "A"
print(grade.count("A"))  # Output: 3

# Question: 4
# Write a program to store the above values in a list & sort them from "A" to "D".

grade = ("C", "D", "A", "B", "B", "A")  # Tuple containing grades

# Converting tuple to list
grade_list = list(grade)

# Sorting the list in alphabetical order
grade_list.sort()

# Printing the sorted list
print(grade_list)  # Output: ['A', 'A', 'B', 'B', 'C', 'D']
