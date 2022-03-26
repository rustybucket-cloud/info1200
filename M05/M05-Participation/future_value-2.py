#!/usr/bin/env python3
import validate as v #import statement
print("Pattons's Validate Future Value App") #display app title

#calculate the future value of investment based on monthly investment, interest, and years
def calculate_future_value(monthly_investment, yearly_interest, years): #define function
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000) #uses get_float function. Parameters: prompt, minumum, maximum
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15)
        years = v.get_int("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
