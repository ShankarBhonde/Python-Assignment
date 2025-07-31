# # -*- coding: utf-8 -*-
# """
# Created on Mon Jul 28 12:02:19 2025

# @author: 91957
# """

# WAP to remove to find duplicates elements in list,
l1=[20,10,30,50,40,10]
store=[]
for i in l1:
    if l1.count(i)>=2 :
        store.append(i)
        l1.remove(i)
print("duplicate value:",store)
print("unique value: ", l1)   
        


# 2. WAP to sort the given list
l1=[20,10,30,50,40]
l1.sort()
print(l1)

# 3. WAP to create a list such that new list contains alternate even and odd from given list
l1=[2,4,6,8,10,1,3,5,7,9]
newlist=[]
for i in l1:
    pass
    if i%2==0:
        pass



# 4. Write a Python program to get the largest number from a list.
l1=[20,10,30,50,40]
#option 1
print(max(l1))

#option 2
max_value=l1[0]
min_value=l1[0]
for i in l1:
    if max_value<i:
        
        max_value=i
    if min_value>i:
        min_value=i
print("max_value : ",max_value)

# 5. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#                            Expected Output : ['Green', 'White', 'Black']

l2=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#option 1
print(l2[1:4])

#option 2
store=[]
for i in l2:
    if i in ['Green','White','Black']:
        store.append(i)
print(store)        
        
        

# 6. Write a Python program to find the list of words that are longer than given words
#  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Input → red
# i want in the form of list output
user=input("enter any string")

size=len(user)
print(size)

color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
store=[]
for i in color:
    if len(i)>size:
        store.append(i) # if condtion will be true then append the value in store variable
           
print(store)        
        








