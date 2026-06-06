# Area of rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print("Area of rectangle:", area, "\n")

# Simple Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time of interest: "))
simple_interest = (principal * rate * time) / 100
print("Simple interest:", simple_interest, "\n")

# Temperature from Celsius to Fahrenheit
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print("Temperature in fahrenheit:", temp_fahrenheit, "\n")

# Average of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
avg = (num1 + num2 + num3) / 3
print("Average of 3 numbers is", avg, "\n")

# Square and cube of a number
num = float(input("Enter a number: "))
num_square = num**2
num_cube = num**3
print("Square of", num, "is", num_square)
print("Cube of", num, "is", num_cube, "\n")

# Swapping two numbers without third variable
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("Swapped values are:")
print("a = ", a)
print("b = ", b, "\n")

# Student Report Program

# Taking student details as input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of three subjects
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = (total / 300) * 100

# Displaying student report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Marks in Subject 1:", marks1)
print("Marks in Subject 2:", marks2)
print("Marks in Subject 3:", marks3)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")