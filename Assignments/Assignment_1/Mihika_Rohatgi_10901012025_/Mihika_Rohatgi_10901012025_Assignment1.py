#Q1
print("Q1. Find area of rectangle")
length=int(input("Enter Length of rectangle:"))
breadth=int(input("Enter Breadth of rectangle:"))
area=length*breadth
print("Area of rectangle=",area)

#Q2
print("Q2. Find simple interest")
p=int(input("Enter principle amount:"))
r=int(input("Enter rate of interest:"))
t=int(input("Enter time:"))
si=p*r*t/100
print("Simple interest=",si)

#Q3
print("Q3. Convert temp from celsius to fahrenheit")
c=int(input("Enter temperature in celsius:"))
f=(c*9/5) + 32
print("Temperature in Fahrenheit is:",f)

#Q4
print("Q4. Calc avg of 3 nos.")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
avg=(num1+num2+num3)/3
print("Average of given 3 numbers is:",avg)

#Q5
print("Q5. Find square and cube of a number")
num=int(input("Enter number:"))
sq=num*num
cube=num**3
print("Square of number is:",sq)
print("Cube of number is:",cube)

#Q6
print("Q6. Swap two numbers without third variable")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("Before swapping: first number is ", x,"second number is", y)
x,y=y,x
print("After swapping: first number is ", x,"second number is", y)

#Q7
print("Q7. Create a Student Report Program")
name=input("Enter student name:")
eng=int(input("Enter marks in english:"))
math=int(input("Enter marks in maths:"))
sci=int(input("Enter marks in science:"))
comp=int(input("Enter marks in computers:"))
tot=eng+math+sci+comp 
percent=(tot/400) * 100
print("----------- Student Report -----------")
print("Student Name:", name)
print("Marks in English:", eng)
print("Marks in Maths:", math)
print("Marks in Science:", sci)
print("Marks in Computer:", comp)
print("--------------------------------------------")
print("Total Marks:", tot)
print("Percentage:", percent)
print("--------------------------------------------")














