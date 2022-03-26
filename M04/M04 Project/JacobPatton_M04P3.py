#Name: Jacob Patton
#Class: INFO 1200
#Section: X01
#Professor: Say
#Date: 9/23/2021
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Jacob Patton's Change App") #display app title
print() #empty line

choice = 'y' #sets choice to 'y'
while choice.lower() == 'y': #while choice is 'y'
    cents = int(input("Enter a number of cents (0-99) ")) #set cents to user input
    print() #empty line

    quarters = cents // 25 #calculate the number of quarters
    cents = cents % 25 #set cents to the remainder of cents divided by 25

    dimes = cents // 10 #calculate the number of dimes
    cents = cents % 10 #set cents to the remainder of cents divided by 10

    nickles = cents // 5 #calculate the number of nickles
    cents = cents % 5 #set cents to the remainder of the cents divided by 5

    pennies = cents // 1 #calculate the number of pennies

    print("Quarters: ", quarters) #display quarters
    print("Dimes:    ", dimes) #display dimes
    print("Nickles:  ", nickles) #display nickles
    print("Pennies:  ", pennies) #display pennies

    print() #empty line
    choice = input("Continue? (y/n) ") #input to run program again
    print() #empty line
print("Bye!") #display bye message