# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 11:45:11 2025

@author: 91957
"""

"""

#WAP to check entered number is divisible by 5 or not

num=int(input("enter the number : "))
if(num%5==0):
    print(f"{num} is divisible by 5")
    
else:
    print("its not divisible by 5")    


'''WAP to Accept the bike price from user & add road tax as follows
 
     Price > 80000   15 % TAX
     Price > 40000 & <80000  10% TAX
     Else                       5% TAX '''
     
     
price=int(input('enter your bike price value: '))
Tax=0
if(price>80000):
    Tax=price*0.15
    print("your Tax is : ", Tax)
    print("your total amount is : ",price+Tax)
     
elif price>40000 and price <=80000:
    Tax=price*0.1
    print("your Tax is : ", Tax)
    print("your total amount is : ",price+Tax)
else:
    Tax=price*0.05
    print("your Tax is : ", Tax)
    print("your total amount is : ",price+Tax)     
     
#Write a program that displays the day of the week corresponding to the number entered. i.e., 1 - "Monday", 2- "Tuesday" and so on

day=int(input("enter the day's number 1-7 : "))

if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday") 
    
elif day==4: 
    print("thusday") 
    
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday") 
else:
    print("out of range, sorry")    



"""

#Write a Python program to input electricity consumption unit and calculate totalel ectricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit 
# For unit above 250 Rs. 1.50/unit 
# An additional surcharge of 20% is added to the bill 
'''
unit=int(input("enter your electricity unit"))
total_amount=0
if unit<=50:
    total_amount= unit*0.50
elif unit>50 and unit<=150:
    total_amount=(50*0.50) + (unit-50)*0.75 
elif unit>150 and unit<=250:
    total_amount=(50 * 0.5)+(100 * 0.75)+(unit-150)*1.20
    
elif unit>250:
    total_amount=(50 * 0.5)+(100 * 0.75)+(100*1.20)+(unit-250)*1.50
    
print(total_amount)    
total_amount+=total_amount * 0.20
    

print(f'your total electricity amount is : {total_amount}')

'''
'''
Accept two numbers from user, give below option like
 
Add
Sub
Mul
Div
Floor div
Exponentiation 
Ask user to select the number & based on that calculate the operation
'''


num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
print("for addition press 1 \n for substraction press 2 \n for multiplication press 3 \n for division press 4 \n for floor division press 5 \n for expontiation press 6 \n for modulus press 7 ")
press =int(input("enter the pressing number"))
if(press==1):
    print(num1+num2)
elif (press==2):
    print(num1-num2)
    
elif press==3:
    print(num1*num2)
elif press==4:
    print(num1/num2)
elif press==5:
    print(num1//num2)
elif press==6:
    print(num1**num2)
elif press==7:
    print(num1%num2) 
else:
    "not match"    
    
    
    
    
    
    
    
    
