# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 11:30:24 2025

@author: 91957
"""

# Write a Python program to create a tuple.
tup1=(45,6,1,2)
print(tup1)


# Write a Python program to create a tuple with different data types
tup2=(4,7,"Shankar",8,"red")
print(tup2)
print(type(tup2))


# Write a Python program to unpack a tuple in several variables.
def unpack(tup1,tup2):
    return tup1,tup2

result=unpack((1,2,3,4,5),(5,6,7,8,9)) #pack 
t1,t2=result #unpack
print("unpack :++++++++++++++++++++++++++ ")
print("unpack t1 :",t1)
print("unpack t2 :",t2)
print(result)


# Write a Python program to add an item in a tuple.
tup2=(4,7,"Shankar",8,"red")
list3=list(tup2)
#print(tup3)
list3.append("python")#option 1
print(list3)
list3.insert(1,12) #option 2
print(list3)
tup2=tuple(list3)#conversion list to tuple
print(tup2)


# Write a Python program to convert a tuple to a string.
tup2=(4,7,"Shankar",8,"red")
string=str(tup2)
print(type(string))

# Write a Python program to reverse a tuple.
tup2=(4,7,"Shankar",8,"red")
print(tup2[::-1])

# Write a Python program to convert a list to a tuple.
list1=[4,5,6,2,"python"]
tuple1=tuple(list1)#conversion list to tuple
print(type(tuple1))

# Write a Python program to remove an item from a tuple.
tup2=(4,7,"Shankar",8,"red")
list2=list(tup2)
list2.remove("red")
tup2=tuple(list2)
print(tup2)

# Write a Python program to slice a tuple.
tup2=(4,7,"Shankar",8,"red")
print(tup2[:2])
print(tup2[1: :1])
print(tup2[::-1])

