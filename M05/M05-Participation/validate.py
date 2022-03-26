#Jacob Patton validation file for the Future Value App

#validates if a user input is between a min and max
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt)) #turns user input into a float
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less thatn or equal to", high)

def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less thatn or equal to", high)

def main():
    choice = 'y'
    while choice.lower() =='y':
        valid_number = get_float("Enter number:", 0, 1000)
        print("Valid number = ", valid_number)

        valid_integer = get_int("Enter integet:",0,50)
        print("Valid integet = ", valid_integer)
        print()

        choice = input("Repeat? (y/n):")
    print("Bye!")

if __name__ == "__main__":
    main()
