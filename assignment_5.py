# # -*- coding: utf-8 -*-
# """
# Created on Wed Jul 23 12:28:08 2025

# @author: 91957
# """


# print its index + char  enumerate() --> 
name="Shankar"
for index,char in enumerate(name):
    print(f"{index}={char}")
    
#WAP even index letters:
print("even index letter")
for index,char in enumerate(name):
    if index%2==0:
        print(f"{index}={char}")


# 1.      Python program to remove given character from String.
string="shankar"
char='r'
print("removed char from given string :",string.replace(char,""))

# 2.     Python Program to count occurrence of a given characters in string.
name="Shankar"
print(name.count('a'))


# 3.     Python program to check a String is palindrome or not.
name="nitin"

if name==name[::-1]:  #reverse the letters by using indexing
    print("palindrome")
    
else:
    print("not palindrome")    

# Python program to check given character is vowel or consonant.

char='a'
if char in 'aeiou':
    print("vowels")
    
else :
    print("consonant")    

# Python program to check given character is digit or not.
# Python program to check given character is digit or not using isdigit() method.
name="12345"
print(name.isdigit())
name="shankar123"
print(name.isdigit())

# Python program to replace the string space with a given character.
name=" shankar "

print(name.replace(" ","@"))

# Python program to replace the string space with a given character using replace() method.
name=" shankar"
print("without remove space:",name)
print(name.replace(" ",""))

# Python program to convert lowercase char to uppercase of string.
name="shankar"
print("lowercase:",name.lower())
print("uppercase:",name.upper())
# Python program to convert lowercase vowel to uppercase in string.

name="shankar"
for ch in name:
    if ch in 'aeiou':
        print(ch.upper())

# Python program to delete vowels in a given string.

text = input("Enter a string: ")

# Create a new string without vowels
no_vowels = ""
for char in text:
    if char not in 'aeiouAEIOU':
        no_vowels += char
print("String without vowels:", no_vowels)

# Python program to count Occurrence Of Vowels & Consonants in a String.
name="shankar"
v_count=0
c_count=0
for ch in name:
    if ch in 'aeiouAEIOU':
        v_count+=1
    else:
        c_count+=1
print("vowels : ",v_count)
print("consonants: ",c_count)
