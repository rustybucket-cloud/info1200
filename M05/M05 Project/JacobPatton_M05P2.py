#Name: Jacob Patton
#Class: INFO 1200
#Section: X01
#Professor: Say
#Date: 10/2/2021
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Jacob Patton's Feet/Meters Converter")
print()

import JPconverter as c

#displays welcome message
def fm_welcome():
    print("Jacob's Feet and Meters Converter")
    print()

#display selection menu
def fm_menu():
    print("Conversion Menu: \n a.Feet to Meters \n b.Meters to Feet")

#main function, user choses which conversion to make,inputs unit to convert, convrsion is displayed
def main():
    fm_welcome()
    while True:
        fm_menu()
        choice = input("Select a conversion (a/b): ")
        print()

        #runs desired conversion based on user input
        if choice == 'a':
            feet = float(input("Enter feet: "))
            meters = c.to_meters(feet) #converts feet input to meters
            print(round(meters, 2), "meters")
        elif choice == 'b':
            meters = float(input("Enter meters: "))
            feet = c.to_feet(meters) #converts meters input to feet
            print(round(feet, 2), "feet")
        else:
            print("You did not enter a valid selection")
        
        more = input("\nWould you like to perform another conversion? (y/n): ")
        print()

        #if input is not y, end function
        if more.lower() != 'y':
            print("Thanks, bye!")
            break

if __name__ == "__main__": main()
