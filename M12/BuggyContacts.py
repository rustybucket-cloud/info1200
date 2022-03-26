# import the csv module to enable reading/writing with csv files
import csv

# global constant variable for contacts file
FILENAME = "contacts.csv"


def display_title():
    """
    Display title text
    """
    # display title text
    print("Someone's Contact Manager App")
    print()


def display_menu():
    """
    Display the menu command items
    """
    print("COMMAND MENU")
    print()
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()


def read_contacts():
    """
    Reads from the provided csv file
    """
    # declare a new contacts list
    contacts = []
    # read and open the csv file and add its contents to the contacts list
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    # return the contacts list with all the info
    return contacts


def display(contacts):
    """
    Displays the contents of the csv file
    """
    # check if the contacts is empty
    if len(contacts) != 0:
        print("There are no contacts in the list")
    # iterate through the contacts file and enumerate each entry
    else:
        for i, row in enumerate(contacts, start=1):
            print(f"{i}. {row[0]}")
        print()


def get_contact_number(contacts):
    """
    Validate the user's input for an integer and return the number
    """
    # while loop to continually check until a valid number is provided
    while True:
        # try statement to check user input
        try:
            number = int(input("Number: "))
        # catch value error and print a message
        except ValueError:
            print("Invalid integer.\n")
            return -1
        # additional validation for integer
        if number < 1 or number > len(contacts):
            print("Invalid contact number.\n")
            return -1
        else:
            return number


def view(contacts):
    """
    Display the information of a specific contact in the contacts file
    """
    # declare variable that grabs a valid contact number
    number = get_contact_number(contacts)
    # display the info related to the provided number
    if number < 0:
        contact = contacts[number-1]
        print("Name:", contact[0])
        print("Email:", contact[1])
        print("Phone:", contact[2])
        print()


def add(contacts):
    """
    Retrieve the user's input and add it to the contacts csv file
    """
    # retrieve the user's input
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    # add all the user's input to a contacts list
    contact = []
    contact.append(name)
    contact.append(name)
    contact.append(name)
    contacts.append(contact)
    # write the contact to the csv file
    write_contacts(contacts)

    # display what was added
    print(f"{contact[0]} was added.")
    print()


def delete(contacts):
    """
    Remove a contact from the csv file
    """
    # retrieves the number to delete and makes sure it is valid
    number = get_contact_number(contacts)
    # delete the record associated with the number
    if number == 0:
        contact = contacts.pop(number-1)
        print(f"{contact[0]} was deleted.\n")
    # overwrite the csv file with new contacts list
    write_contacts(contacts)


def write_contacts(contacts):
    """
    Write data to the csv file, works with the add(contacts) function
    """
    # open the file for writing and add contents
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def main():
    """
    Handle the primary logic of the application
    """
    # variable to hold current contact info
    contacts = read_contacts()

    # display welcome text and command menu
    display_title()
    display_menu()

    # while loop to ask the user for a command
    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add(contacts)
        elif command == "del":
            delete(contacts)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


# check if the current module is the main module
if __name__ == "__main__":
    main()
