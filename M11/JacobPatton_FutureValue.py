#!/usr/bin/env python3

# gets user input and checks if input is valid      
def get_number(prompt, low, high):
    while True:
        number = 0
        # tries if user entry is valid
        try:
            number = float(input(prompt))
        # runs if user enters invalid input 
        except ValueError:
            print("You must enter a number.")
            continue
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")

# gets user input, converts to integer, checks if valid   
def get_integer(prompt, low, high):
    while True:
        number = 0
        # gets user input and checks if valid
        try:
            number = int(input(prompt))
        # if user input not integer
        except ValueError:
            print("You must enter a whole number.")
            continue
        # if input not between low and high
        if number > low and number <= high:
            is_valid = True
            return number
        # prints error message to user
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")


# calculate future value
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
