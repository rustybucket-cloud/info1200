#!/usr/bin/env python3

# display a welcome message
print("Jacob Patton's Miles Per Gallon application") #print application title
print() #print blank line

another_trip = 'y' #set another_trip inital value
while another_trip == "y": #start while loop
    cost_per_gallon = float(input("Enter cost per gallon:      ")) #set cost_per_gallon to user input and covert it to float
    # get input from the user
    miles_driven = float(input("Enter miles driven:         ")) #set miles_driver to user input and covert it to float
    gallons_used = float(input("Enter gallons of gas used:  ")) #set gallons_used to user input and covert it to float
    print() #empty line

    if miles_driven <= 0: #if miles_driven is less than or equal to 0
        print("Miles driven must be greater than zero. Please try again.") #display error message
    elif gallons_used <= 0: #if gallons_used is less than or equal to 0
        print("Gallons used must be greater than zero. Please try again.") #display error message
    elif cost_per_gallon <= 0: #if cost_per_gallon is less than or equal to 0
        print("Cost per gallon must be greater than zero. Please try again.") #display error message
    else: #else statement
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2) #set mpg to miles_driven divided by gallons_used and round it to 2 decimals
        total_gas_cost = round((cost_per_gallon * gallons_used), 2) #set total_gas_cost to cost_per_gallon times gallons_used and round it to 2 decimals
        cost_per_mile = round((total_gas_cost / miles_driven), 2) #set cost_per_mile to total_gas_cost divied by miles_driven and round it to 2 decimals
        print("Miles Per Gallon:          ", mpg) #display mpg
        print("Total Gas Cost:            ", total_gas_cost) #display total_gas_cost
        print("Cost Per Mile:             ", cost_per_mile) #display cost_per_mile
        print() #display message

    another_trip = input("Get entries for another trip (y/n)?") #set another_trip to user input to continue or end loop

    print() #empty line
print("Bye") #display bye message



