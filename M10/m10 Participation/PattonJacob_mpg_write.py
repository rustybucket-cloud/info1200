#!/usr/bin/env python3
import csv

#gets the number of miles driver
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven

#gets the number of gallons used         
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def main():
    entries = [] #all entries, will be added to csv file
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":
        data = [] # this entry, added to entries list 
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        # adds data to list that will be added to csv
        data.append(miles_driven)
        data.append(gallons_used)
        data.append(mpg)
        entries.append(data)

        more = input("More entries? (y or n): ")
    # appends data to csv file
    with open("trips.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(entries)
    print("Bye!")

if __name__ == "__main__":
    main()

