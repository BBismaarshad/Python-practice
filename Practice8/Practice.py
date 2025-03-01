# Question1: 
# Print number form 1 to 100. 
i = 1 
while i <= 100:
    print(i)
    i += 1

# Question2: 
#Print number from 100 t0 1.
i = 100
while i >= 1:
    print(i)
    i -= 1

# Question3: 
#print the  multiplication table of a number.
    n = int (int(input("Enter number:")))
    i = 1
    while i <= 10:
        print(f"{n}*{i}={n*i}")
        i += 1

# Question4:
#print the elements of the following using a loop->:[1,4,9,16,25,36,46,64, 81, 100]
nums = [1,4,9,16,25,36,46,64, 81, 100] 
idex =0
while idex<len (nums):
    print(nums[idex])
    idex += 1

# Question5:
#Search for a number x in this tuple using loop->:[1,4,9,16,25,36,46,64, 81, 100]
nums = (1,4,9,16,25,36,46,64, 81, 100)
x =36
i =0
while i<len(nums):
    if (nums[i]== x):
        print("Fourd at idex",i)
        i += 1