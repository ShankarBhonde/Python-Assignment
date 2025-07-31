# # -*- coding: utf-8 -*-
# """
# Created on Fri Jul 25 11:34:49 2025

# @author: 91957
# """

# Write a program to create a function that takes two arguments, name and age, and print their value.
def enfo(name,age):
    print(f"my name is {name} and age is {age}")
    
enfo("shankar", 23)    
# Write a program to create function calculation() such that it can accept two variables and calculate addition
# and subtraction. Also, it must return both addition and subtraction in a single return call
def calculation(num1,num2):
    addition=num1+num2
    sub=num1-num2
    print("addition is :",addition)
    print("substraction is : ",sub)
    return addition,sub

calculation(12, 10)
print(calculation(12, 2))

# Write a program to create a function show_employee() using the following conditions.

# ●  	It should accept the employee’s name and salary and display both.
# ●  	If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name,salary=40000): #default salary is 40000
    print(f"employee name is {name} and salary is {salary}")
    
# name=input("enter the name: ")
# salary=float(input("enter the salary : "))

show_employee("Shankar")    
# 4.	Accept a number from the user, create a function isPrime(), which accepts a number from a parameter &
# check prime or not. If number is prime return True & number else return false & number
count=0
def isPrime(number):
    
    if(number%2==0):
        count+=1
def display():
    if count==2:
        return True
    else :
        
        return False
        
print(isPrime(5))        
# 5.	Create menu driven calculation (add,sub,multiply, divide, mod) using function
# def calculation():

def menu():
    
    choice=input("press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division\n press 5 for mod")
    num1=10
    num2=5
    match choice:
        case 1:
            print("addition is :",num1+num2)
             
        case 2:
            print("substraction is : ",num1-num2)
             
        case 3:
            print("multiplication is : ",num1*num2)
        case 4:
            
            if num2 !=0:
                
                print("cant divided by zero")
                
            else :
                
                print("division is :",num1/num2)

menu()
                
# 6.	Create a function to accept a number & return its factorial

def fact(n): #using resursion
    if n==1:
        return 1

    else :
        return n*fact(n-1)

print(fact(5))    
    
# 7.	Create a function that accept student data, calculate the total & percentage, return total & percentage
def student_result(name, m1, m2, m3):
    total = m1 + m2 + m3
    percentage = (total / 300) * 100
    return f" the total marks is {total} and  percentage : {percentage}"


name = input("Enter student name: ")
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))
print(student_result(name, m1, m2, m3))
# 8.	Create a login function, that accept username & password, if username is ‘admin’ &
 # password is ‘admin@123’ then return true, else return false
 
def authentication(username,password):
     if username=='admin' and password=='admin@123':
         return True
     else:
         return False
     
username=input("enter the yourname :")
password=input('enter the password :')
print(authentication(username, password))        