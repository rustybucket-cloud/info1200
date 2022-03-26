#Name: Jacob Patton
#Class: (INFO 1200)
#Section: (X01)
#Professor: Say
#Date: 9/12/2021
#Project #:2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Jacob Patton Registration App") #App title
print() #empty line

#User Data
firstName = input("First Name: ") #first name input
lastName = input("Last Name: ") #last name input
birthYear = input("Birth Year: ") #birth year input
print() #empty line

print("Welcome " + firstName + " " + lastName + "!") #welcome message
print() #empty line

temporaryPassword = firstName + "*" + birthYear #generate temporary password
print("Your registration is complete.") #display registration complete message
print("Your temporary password is: " + temporaryPassword) #display temporary password
