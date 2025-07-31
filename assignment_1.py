# # # -*- coding: utf-8 -*-
# # """
# # Created on Thu Jul 17 11:40:42 2025

# # @author: 91957
# # """

# # #Assessments

# # 1. Write a Python program to enter two numbers and find their sum.

# # 2. Write a Python program to enter two numbers and perform all arithmetic
# # operations.
# # 3. Write a Python program to enter length and breadth of a rectangle and find its Area
# # 4. Write a Python program to enter base and height of a triangle and find its area..
# # 5. Write a python Program to calculate Square of given number
# # 6. Write a python Program to calculate cube of given number
# # 7. Write a Python program to enter marks of five subjects and calculate total, and percentage.
# # 8. Write a Python program to enter P, T, R and calculate Simple Interest.
# # 9. Write a Python program to enter length and breadth of a rectangle and find its perimeter.

# solutions:
#     Assessments

# 1. Write a Python program to enter two numbers and find their sum.

a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
sum=a+b
print(a+b)

# 2. Write a Python program to enter two numbers and perform all arithmetic
# operations.
'''
print("adddtion :",a+b)
print("substraction :",a-b)
print("division :",a/b)
print("multiplication :",a*b)
print("floor division :",a//b)
print("modulus",a%b)
print("expotiation :",a**b)
'''


# 3. Write a Python program to enter length and breadth of a rectangle and find its Area
length=float(input("enter the length : "))
breadth=float(input("enter the breadth : "))
area_of_recatngle=length*breadth
print(area_of_recatngle)

# 4. Write a Python program to enter base and height of a triangle and find its area..
base=float(input("enter the base value :"))
height=float(input("enter the height value :"))
area_of_triangle=(1/2)* base *height         # you can also use 0.5
print(area_of_triangle)

# 5. Write a python Program to calculate Square of given number
num1=5
print("square of 5 is :", num1**2)

# 6. Write a python Program to calculate cube of given number
num2=10
print("cube of 10 is : ",num2**3)


# 7. Write a Python program to enter marks of five subjects and calculate total, and percentage.
sub1,sub2,sub3,sub4,sub5=70,85,96,86,65
total_marks=sub1+sub2+sub3+sub4+sub5
print(f"total marks is : {total_marks}")
#option 1
percentage1=(total_marks/500)*100
print(percentage1)
# option 2
percentage=total_marks/5  #402/500=0.804
print("percentage : ", percentage)

# 8. Write a Python program to enter P, T, R and calculate Simple Interest.
p_amount=int(input("enter your amount : "))
time=float(input("enter your duration : "))
rate=float(input("enter your rate : "))

simple_Interest=(p_amount*rate*time)/100
print("simple interest is :" , simple_Interest)
#total amount
total_amount=p_amount+simple_Interest
print("total amount :",total_amount)

# 9. Write a Python program to enter length and breadth of a rectangle and find its perimeter.
lenght1=length
breadth1=breadth
area_of_perimeter=2*(lenght1+breadth1)
print("area of perimeter is :" ,area_of_perimeter)     
