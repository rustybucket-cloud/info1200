#Name: Jacob Patton
#Class: INFO 1200
#Section: X01
#Professor: Say
#Date: 11/6/2021
#Project #: M09
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#displays application title
def display_title():
    print("Jacob Patton's Wizard Inventory Game")
    print()

#displays a menu for what to do
def display_menu():
    print("COMMAND MENU")
    print()
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")

#displays all the items in the wizards inventory
def show(inventory):
    for number, item in enumerate(inventory, start=1):
        print(f"{number}, {item}")
    print()

#adds a new item to wizard's inventory
def grab_items(inventory):
    if len(inventory) >= 4:
        print("You can't carry any more items. Drop something first. \n")
    else:
        item = input("Name: ")
        inventory.append(item)
        print(f"{item} waas added. \n")

#edits an item in wizard's inventory
def edit_item(inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("Invalid item number. \n")
    else:
        item = input("Updated name: ")
        inventory[number-1] = item
        print(f"item number {number} was updated. \n")

#removes item from wizard's inventory
def drop_item(inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("Invalid item number.\n")
    else:
        item = inventory.pop(number-1)
        print(f"{item} was dropped.\n")

#main function
def main():
    display_title()
    display_menu()

    inventory = ["staff", "hood", "umbrella"]

    while True:
        command = input("Command: ")
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab_items(inventory)
        elif command == "edit":
            edit_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again. \n")
    print("Bye!")

if __name__ == "__main__":
    main()