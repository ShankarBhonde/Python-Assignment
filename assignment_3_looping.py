# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 11:23:54 2025

@author: 91957


"""


'''

Separate each digit & cube and addition have a same number

153 = (1*1*1)+(5*5*5)+(3*3*3)

153 =  1 + 125 + 27

153 = 153


'''
#this question type of aramstrong number
num=num1=1534
temp=num
value=0

count=0
while num1>0:
    count=count+1
    num1=num1//10
    
while num>0:
    digit=num%10
    value=value+digit**count
    num=num//10
    
if value==temp:
    print("its armstrong number")

else :
    print("not armstrong number")   
  
    
# count vowels
text=input("enter your name : ")
count=0
vowels="aeiouAEIOU"
for char in text:
    if char in vowels:
        count+=1
print("the count is : ", count)   
#     WAP to print even numbers from 121 to 229 using a for loop.

i=121
while i<229:
    if i%2==0:
        print(i,end=" ")
    i=i+1    

#  WAP to print odd numbers from 521 to 229 using a while loop.
print("\n odd number")
i=521
while i>229:
    if i%2 !=0:
        print(i,end=" ")
    i=i-1    
#  Write a Python program to print all alphabets from a to z  using  for loop
print("print a to z char")
for i in range(97, 123):  # ASCII values of a = 97 and z = 122
    print(chr(i), end=' ')
    
    
#  Write a Python program to find the sum of all even numbers between 1 to n.
n=int(input("\nenter the value"))
i=1
store=0
while i<=n:
    if i%2==0:
        store=store+i
    i=i+1    
        
print("sum of even number is : ",store)       
#  Write a Python program to find the sum of all odd numbers between 1 to n.
number=int(input("enter the number : "))
i=1
store=0
while i<=number:
    if i%2 !=0:
        store=store+i
        
    i=i+1
print("sum of odd number is : ",store)        
#  Write a Python program to count number of digits in any number
num=input("enter the your count number : ")
print(len(num)) #len function use for string value not interger value
#another method
count=0
num1=int(input("enter the count number : "))
while num1>0:
    count=count+1
    num1=num1//10
print("count is : ",count)    
# WAP to print table of given no
table=int(input("enter table number"))
i=1
while i<=10:
    print(i*table)
    i=i+1
# WAP to print squares from 1 to20
i=1
while i<=20:
    print(f" square of {i} is :" , i**2)
    i=i+1
    