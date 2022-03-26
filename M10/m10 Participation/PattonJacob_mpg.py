#!/usr/bin/env python3
import csv

FILE_NAME = "trips.csv"

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def write_trips(entries):
    # create writer object to write to trips.csv file
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(entries)

def read_trips():
    # create reader object to read data from reader.csv file
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        trips = []
        # iterate through data and add to trips list
        for row in reader:
            trips.append(row)
        return trips

# read trips and display them
def list_trips(trips):
    print("Distance:\tGallons\t\tMPG")
    # iterate through trips list
    for trip in trips:
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
    print()

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # retrieves data from csv file
    trips = read_trips()

    more = "y"
    while more.lower() == "y":
        # prints out each trip
        list_trips(trips)
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)

        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # adds current trip to trips list
        single_trip = [miles_driven, gallons_used, mpg]
        trips.append(single_trip)

        more = input("More entries? (y or n): ")
    
    # writes trips list to csv file
    write_trips(trips)

    print("Bye!")

if __name__ == "__main__":
    main()

