#!/usr/bin/env python3
print("Jacob Patton's Rectangle App") #display full name and title

# display a welcome message
print("The Miles Per Gallon program") #display app title
print() #display blank line

# get input from the user
length= float(input("Please enter the length:\t\t")) #declare and set length variable to user input
width = float(input("Please enter the width:\t\t")) #declare and set width variable to user input

# calculate area and perimeter
area = length * width #declare and set area variable as length time width
perimeter = (length * 2) + (width * 2) #declare and set perimeter as 2 time length plus 2 times width
            
# format and display the result
print() #display blank line
print("Area:\t\t\t\t" + str(area)) #display area variable
print("Perimeter:\t\t\t" + str(perimeter)) #display perimeter variable
print() #display blank line
print("Thanks for using this progran!") #display thank you message
