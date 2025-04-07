import datetime

# This program prints the name and the current year
"""name = "Segun Ade-Martins"
# year = datetime.datetime.now().year

# print(name)
# print(year)
# print(name,  year)"""

#Workbook Activity Day 2 Task 1
# FizzBuzz

#Test numbers in a range
# Loop through numbers from 1 to 100 (inclusive)
"""for number in range(1, 101):
    # Check if the number is divisible by 3 and 5, first
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        # If the number is divisible by 3, print "Fizz"
    elif number %  3 == 0:
        print("Fizz")
        # If the number is divisible by 5, print "Buzz"
    elif number % 5 == 0 and number % 5 == 0:
        print("Buzz")
    else:
        # If none of the above conditions are met, print the number itself, default case
        print(number)"""

# Calculating perimeter of a rectangle with user input for arguments
"""def calculate_rectangle_perimeter():
  #This function calculates and prints the perimeter of a rectangle.
  length = float(input("Enter the lenght of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))
  if length <= 0 or width <= 0:
        print("Length and width must be positive numbers.")
        
  else:
        perimeter = 2 * (length + width)
        print("The perimeter of the rectangle is:", perimeter)
  
calculate_rectangle_perimeter()    
    

# Calculating perimeter of a rectangle with arguments passed to the function
def calculate_rectangle_perimeter2(length, width):
  #This function calculates and prints the perimeter of a rectangle.
  if length <= 0 or width <= 0:
        print("Length and width must be positive numbers.")
        
  else:
        perimeter = 2 * (length + width)
        print("The perimeter of the rectangle is:", perimeter)
  
calculate_rectangle_perimeter2(3,4)"""  

test_ratings = [1,2,3,4,5]

test_liked = [i>= 4 for i in test_ratings]
print(test_liked)
