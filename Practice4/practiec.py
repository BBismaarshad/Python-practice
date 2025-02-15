
# Question: 1
# Write a program to find the greatest of 3 numbers entered by the user.

# Taking three numbers as input from the user
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

# Checking which number is the greatest
if a >= b and a >= c:
    print("First number is largest:", a)
elif b >= c:
    print("Second number is largest:", b)
else:
    print("Third number is largest:", c)


# Question: 2
# Write a program to check if a number is a multiple of 7 or not.

# Taking input from the user
x = int(input("Enter a number: "))

# Checking if the number is a multiple of 7
if x % 7 == 0:
    print("The number is a multiple of 7")
else:
    print("The number is NOT a multiple of 7")

