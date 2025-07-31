# # -*- coding: utf-8 -*-
# """
# Created on Tue Jul 22 18:39:57 2025

# @author: 91957
# """

# #check anagram or not
# str1=input("enter the first word : ")
# str2=input("enter the second word : ")

# #remove spaces and apply lower case
# str1=str1.replace(" ","").lower()
# str2=str2.replace(" ","").lower()
# #check sorted and anagram
# if sorted(str1)==sorted(str2):
#     print("anagram")
# else:
#     print("not anagram")    

#WAP to check the armstrong number  or not 

num=num1=153
count=0
temp=num
while num>0:
    count=count+1
    num=num//10
print(count)   
store=0
while num1>0:
    r=num1%10
    store=store+r**count
    num1=num1//10
print(store)    
#i will check armstron or not 
if temp==store:
    print("armstron")
else :
    print("not armstrong") 


#WAP to fabonacci series (addition of adjecent number) # i want first 10 fabonacci number

a=0
b=1
print(a,b,end=" ")
i=1
while i<10:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1


    
    
    