# This is a Python script.
from colored import fg, attr

# set a color reset using colored library
reset_color = attr("reset")
# some variables to make coding colored text easier, using colored library
yellow_text = fg(3)
green_text = fg(2)
red_text = fg(1)
blue_text = fg(4)
cyan_text = fg(6)
sea_green = fg(78)


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
    print(f"{green_text}The result of the addition is: {sea_green}{result}{reset_color}")


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
    print(f"{green_text}The result of the multiplication is: {sea_green}{result}{reset_color}")


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
                print(f"{red_text}Invalid number or command\nThe answer didn't affect your calculation ")
                print(f"{blue_text}-={reset_color}" * 20, )
            # if everything goes ok, it adds the user input to a list called "List_of_Input_numbers"
            else:
                List_of_Input_numbers.append(input_number)
    # returns a list with numbers that the user input
    return List_of_Input_numbers


if __name__ == '__main__':
    # print a colored message
    print(f"{yellow_text}Type '=' to show the addition and multiplication of the numbers you typed{reset_color} ")
    # call the function for getting unlimited number inputs
    List_of_Input_numbers = get_number_input()
    # call the function to make an addition with the numbers the user input
    add(List_of_Input_numbers)
    # call the function to multiply the number that the user input
    multiply(List_of_Input_numbers)

# The Code editor I used is Pycharm
# https://www.jetbrains.com/pycharm/
