#!/usr/bin/env python3
print("Jacob Patton's MPG App") #print first and last name and string MPG App

# display a welcome message
print("The Miles Per Gallon program") #display program title
print() #blank line

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t")) #set miles driven to user input
gallons_used = float(input("Enter gallons of gas used:\t")) #set gallons used to user input
cost_per_gallon = float(input("Enter cost per gallon:\t\t")) #set cost_per_gallon as user input

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1) #calculate mpg and round it to 1 decimal
            
# format and display the result
print() #print blank line
print("Miles Per Gallon:\t\t" + str(mpg)) #print mpg
print("Total Gas Cost:\t\t\t" + str(round(gallons_used * cost_per_gallon, 1))) #print Total Gas Cost
print("Cost per Mile:\t\t\t" + str(round(cost_per_gallon / mpg, 1))) #print cost per mile
print() #print blank line
print("Bye") #print Bye


