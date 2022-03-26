#Name: Jacob Patton
#Class: INFO 1200
#Section: X01
#Professor: Say
#Date: 10/2/2021
#Project #: MO5_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Jacob Patton's Even or Odd Checker")
print()

#checks if number is even, returns true or false
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

#main function, returns if input is even or odd
def main():
    print("Jacob's even or odd checker")
    print()
    my_num = int(input("Enter an integer: "))
    if is_even(my_num):
        print("This is an even number")
    else:
        print("This is an odd number")

if __name__ == "__main__": main()
