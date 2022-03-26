#Name: (Jacob Patton)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Say)
#Date: 11/21/21
#Project #: M11
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv
FILE_NAME = "contacts.csv"

import tkinter as tk
from tkinter import ttk

# display title
def display_title():
    print("Jacob Patton's Contact Manager App")
    print()

# display menu options
def display_menu():
    print("COMMAND MENU")
    print()
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()

# read contacts from csv file
def read_contacts():
    contacts = []
    # add each contact to contacts
    with open(FILE_NAME, "r", newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

# display contacts
def display(contacts):
    for i, row in enumerate(contacts, start=1):
        print(f"{i}. {row[0]}")
    print()

# gets contact by index
def get_contact_numbers(contacts):
    while True:
        try: 
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer\n")
            return -1

        if number < 1 or number > len(contacts):
            print("Invalid contact number. \n")
            return -1
        else:
            return number

# view contact information
def view(contacts):
    number = get_contact_numbers(contacts)
    if number > 0:
        contact = contacts[number-1]
        print("Name:", contact[0])
        print("Email:", contact[1])
        print("Phone:", contact[2])
        print() 

# adds a new contact
def add(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    print()

# write contacts to csv file
def write_contacts(contacts):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# deletes contacts
def delete(contacts):
    number = get_contact_numbers(contacts)
    if number > 0:
        contact = contacts.pop(number - 1)
        print(f"{contact[0]} was deleted. \n")
    write_contacts(contacts)

def main():
    display_title()
    display_menu()
    contacts = read_contacts()
    create_gui(contacts)
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
    print()
    print("Bye!")

if __name__ == "__main__":
    main()