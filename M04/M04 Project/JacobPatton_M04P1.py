#Name: Jacob Patton
#Class: INFO 1200
#Section: X01
#Professor: Say
#Date: 9/23/2021
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Jacob Patton's Letter Grade Conterter") #display title

choice = 'y' #set choice to 'y'
while choice.lower() == 'y': #while choice is 'y'
    print() #blank line
    number = int(input("Enter numerical grade: ")) #set number to user input
    if number >= 94: #if number is equal to or greater than 94
        letter = 'A' #set letter to 'A'
    elif number >= 90: #if number is equal to or greater than 90
        letter = 'A-' #set letter to 'A-'
    elif number >= 87: #if number is equal to or greater than 87
        letter = 'B+' #set letter to 'B+'
    elif number >= 83: #if number is equal to or greater than 83
        letter = 'B' #set letter to 'B'
    elif number >= 80: #if number is equal to or greater than 80
        letter = 'B-' #set letter to 'B-'
    elif number >= 77: #if number is equal to or greater than 77
        letter = 'C+' #set letter to 'C+'
    elif number >= 73: #if number is equal to or greater than 73
        letter = 'C' #set letter to 'C'
    elif number >= 70: #if number is equal to or greater than 70
        letter = 'C-' #set letter to 'C-'
    elif number >= 67: #if number is equal to or greater than 67
        letter = 'D+' #set letter to 'D+'
    elif number >= 63: #if number is equal to or greater than 63
        letter = 'D' #set letter to 'D'
    elif number >= 60: #if number is equal to or greater than 60
        letter = 'D-' #set letter to 'D-'
    elif number <= 70: #if number is equal to or less than 70
        letter = 'E' #set letter to 'E'

    print("Letter grade: ", letter) #display letter
    print() #empty line
    choice = input("Continue? (y/n)") #set choice to user input

print("Bye!") #print bye message