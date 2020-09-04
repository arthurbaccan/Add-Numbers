# This is a sample Python script.
from termcolor import cprint


# Function for addition of unlimited numbers
def add(*nums):
    # make num a global variable, so it can be used out of for loops in the function
    global num
    # assignment of the variables
    count = 0
    result = 0
    # copy all numbers from nums(Numbers) list to num list and check it's length
    for num in nums:
        count += len(num)
    else:
        # make an addition with each number in the num list(that has the inputs from the person using this program)
        # when the first for loop finished being executed
        for c in range(count):
            result += float(num[c])
    cprint(f"The result of the addition is {result}", "green")


# function for make multiplications of unlimited numbers
def multiply(*nums):
    # make num2 a global variable, so it can be used out of for loops in the function
    global num2
    # assignment of the variables
    result = 0
    count = 0
    # First time variable is used to check if it's the first loop in the for loop is being executed.
    first_time = True
    # copy all numbers from nums(Numbers) list to num2 list and check it's length
    for num2 in nums:
        count += len(num2)
    else:
        # make an multiplication with each number in the num list(that has the inputs from the user)
        # when the first "for loop" finishes being executed
        for c in range(count - 1):
            # check if first_time variable is true
            if first_time:
                result = float(num2[c]) * float(num2[c + 1])
                first_time = False
            else:
                result = result * float(num2[c + 1])
    # print colored text
    cprint(f"The result of the multiplication is {result}", 'green')


# function for getting number inputs from the user
def get_number_input():
    # make List_of_Input_numbers a global variable, so it can be used in all indentations of the function
    global List_of_Input_numbers
    List_of_Input_numbers = []
    # while loop for getting an infinite amount of inputs
    while True:
        # variable called number gets a string input from the user
        input_number = str(input("Type a number: "))
        # "if statement" breaks the input loop if "=" is typed
        if input_number == "=" or input_number == "==":
            break
        else:
            # checks to see if a number was typed by the user
            try:
                float(input_number)
            # if a there is ValueError error, the user typed something else than numbers...
            except ValueError:
                cprint("Invalid number or command\nThe answer didn't affect your calculation ", "red")
                cprint("-=" * 20, "blue")
            # if everything goes ok, it adds the user input to a list called "List_of_Input_numbers"
            else:
                List_of_Input_numbers.append(input_number)
    # returns a list with numbers that the user input
    return List_of_Input_numbers


if __name__ == '__main__':
    # print a colored message
    print("type numbers to make calculations with them")
    cprint("Type '=' to show the addition and multiplication results ", 'yellow')
    # call the function for getting unlimited number inputs
    List_of_Input_numbers = get_number_input()
    # call the function to make an addition with the numbers the user input
    add(List_of_Input_numbers)
    # call the function to multiply the number that the user input
    multiply(List_of_Input_numbers)

# The Code editor I used is Pycharm
# https://www.jetbrains.com/pycharm/
