
# Question:1
# Write a program to input user's irst name & print its length.

#  Find the length of a name
name = input("Enter your name: ")  
print("Length of your name is", len(name))  


# Question:2
# Write a program to find the occurrence of "$" in a string.

# Count occurrences of "$" in a string
str_value = "Hi.$Iam  the $ symbol $99.99"  
print(str_value.count("$"))  



# Program 3: Check if a number is even or odd
num = int(input("Enter a number: "))  

if num % 2 == 0:  # "=" ki jagah "==" use karein
    print("EVEN")  
else:
    print("ODD")  
