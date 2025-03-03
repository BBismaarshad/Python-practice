

# Using for and range()

# Question 1: 
# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)  # Print each number from 1 to 100

# Question 2:
# Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)  # Print each number from 100 down to 1

# Question 3:
# Print the multiplication table of a number n.
n = int(input("Enter number:"))  # Get user input for the number to multiply
for i in range(1, 11):
    print(n * i)  # Print the multiplication result for n from 1 to 10
