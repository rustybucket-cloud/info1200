#!/usr/bin/env python3

# display a welcome message
print("Welcome to Jacob Patton's Future Value Calculator") #display title
print() #empty line

choice = "y" #sets default choice to y
while choice.lower() == "y": #while choice is y
    is_valid = True #sets is_value to True
    while is_valid == True: #while is_valid is True
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t")) #set monthly_investment to user input
        if monthly_investment >= 0 and monthly_investment <= 1000: #if monthly_investment is greater than 0 and less than or equal to 1000
            is_valid = False #set is_valid to False
        else: #else statement
            print("Entry must be greater than 0 and less than 1000. Please try again.") #display error message
    is_valid = True #sets is_valid to True
    while is_valid == True: #while is_valid is True
        yearly_interest_rate = float(input("Enter yearly interest rate:\t")) #sets is_valid to user input
        if yearly_interest_rate >= 0 and yearly_interest_rate <= 15: #if yearly_interest_rate is greater than 0 and less than or equal to 15
            is_valid = False #sets is_valid to False
        else: #else statement
            print("Entry must be greater than 0 and less than 15. Please try again.") #display error message
    is_valid = True #sets is_valid to true
    while is_valid == True: #while is valid is True
        years = int(input("Enter number of years:\t\t")) #sets years to user input
        if years >= 0 and years <= 50: #if years is greater than 0 and less than or equal to 50
            is_valid = False #sets is_valid to False
        else: #else statement
            print("Entry must be greater than 0 and less than 50. Please try again.") #display error message
    print() #empty line

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100 #sets monthly_interest_rate to yearly_interest_rate divided by 12 divided by 100
    months = years * 12 #sets month to years times 12

    # calculate the future value
    future_value = 0 #sets future value to 0
    for i in range(months + 1): #for that runs month + 1 number of times
        future_value += monthly_investment #sets future_value to itself plus monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate #sets monthly_interest_amount to future_value times monthly_interest_rate
        future_value += monthly_interest_amount #sets future_value to itself plus monthly_interest_amount

        # display the result
        if i % 12 == 0 and i != 0: #if the remained of i divided by 12 is 0 and i is not 0
            print("Year = ", str(i // 12), "\tFuture value = " + str(round(future_value, 2))) #display year and future value
    print() #empty line

    # see if the user wants to continue
    choice = input("Continue (y/n)? ") #sets choice to user input
    print() #empty line

print("Bye!") #display goodbye message
