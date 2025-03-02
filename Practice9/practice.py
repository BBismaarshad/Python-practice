# Question1:
#Print the elements of the following  list using a loop-> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Define a list of numbers
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Loop through each element in the list
for el in nums:
    # Print the current element in the list
    print(el)


# Question2:
#Search for a number x in this tuple using loop-> [1,4,9,16,25,36,46,64,81,100,49]
nums = (1,4,9,16,25,36,46,64,81,100,49)

# Number to search for in the tuple
x = 49

# Index counter for the loop
idx = 0

# Loop through each element in the tuple
for el in nums:
    # If the element matches the target number
    if el == x:
        # Print the index where the number is found
        print(f"Number found at idx {idx}")
    idx += 1  # Increment index after checking each element
