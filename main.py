# This is a Python script.
from colored import fg, attr

# some variables to make coding colored text easier, using colored library
reset_color = attr("reset")
yellow_text = fg(3)
green_text = fg(2)
red_text = fg(1)
blue_text = fg(4)
cyan_text = fg(6)
sea_green = fg(78)
orange_text = fg(172)
gray_text = fg(7)


# Function for addition of unlimited numbers
def add(nums: list):
    # assignment of result variable that is going to be used later.
    result = 0
    # stores the length of "nums" list in a variable called count
    count = len(nums)
    # adds each number in the "nums" list and store its value in a variable called "result".
    for c in range(count):
        result += float(nums[c])
    # returns the "result" variable
    return result


# Function for subtraction of unlimited numbers
def subtract(minuends: list, subtrahends: list):
    # assignment of variables that are going to be used later
    all_minuends = 0
    all_subtrahends = 0
    # stores the length of "minuends" list in a variable called count_minuends
    count_minuends = len(minuends)
    # adds each number in "minuends" list
    for c in range(count_minuends):
        all_minuends += float(minuends[c])
    # stores the length of "minuends" list in a variable called count_minuends
    count_subtrahends = len(subtrahends)
    # adds each number in "minuends" list
    for c in range(count_subtrahends):
        all_subtrahends += float(subtrahends[c])
    # subtracts the numbers and store the result of the subtraction in a variable called "result".
    result = all_minuends - all_subtrahends
    # returns the "result" variable
    return result


# function that makes multiplications of unlimited numbers
def multiply(nums: list):
    # assignment of the variable that is going to be used later
    result = 0
    # "First_time" variable is used to check if the first loop in the for loop is being executed.
    first_time = True
    # stores the length of "nums" list in a variable called count
    count = len(nums)
    # multiplies each number in the "nums" list(that has the inputs from the user)
    for c in range(count - 1):
        # checks if first_time variable is true
        if first_time:
            result = float(nums[c]) * float(nums[c + 1])
            first_time = False
        else:
            result = result * float(nums[c + 1])
    # returns the "result" variable
    return result


# function for division of unlimited numbers
def division(dividends: list, divisors: list):
    # assignment of the variables that are going to be used later
    sum_dividends = 0
    sum_divisors = 0
    # stores the length of "dividends" list in a variable called "count_dividends"
    count_dividends = len(dividends)
    # stores the length of "divisors" list in a variable called "count_divisors"
    count_divisors = len(divisors)
    # adds each number from the "dividends" list(that has the inputs from the user)
    for c in range(count_dividends):
        sum_dividends += float(dividends[c])
    # adds each number from the "divisors" list(that has the inputs from the user)
    for c in range(count_divisors):
        sum_divisors += float(divisors[c])
    # divides the numbers and store the result of the division in a variable called "result"
    result = sum_dividends / sum_divisors
    # returns the "result" variable
    return result


# function for getting number inputs from the user
# the "message" parameter is going to be displayed to the user
def get_number_input(message="Type a number"):
    # make List_of_Input_numbers a global variable, so it can be used in all indentations of the function
    global list_of_Input_numbers
    list_of_Input_numbers = []
    # while loop for getting an infinite amount of inputs
    while True:
        # variable called number gets a string input from the user
        input_number = str(input(message))
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
                list_of_Input_numbers.append(input_number)
    # returns a list with numbers that the user input
    return list_of_Input_numbers


if __name__ == '__main__':
    # makes a loop that never ends
    # print colored instructions
    print(f'''{gray_text}Instructions: 
Type an command(from the command list below) to chose an mode,
and start doing calculations with unlimited numbers. 
Don't forget to press "enter" after you type a number.
When you finish typing the first set of numbers, enter "=" to type the second set of numbers and when you finish,
enter "=" to show the final result''')
    print('''Subtractions works this way: The first set of numbers you enter(minuends) will be subtracted from the
second set of numbers you type(subtrahends). Example: First set of numbers the user entered(minuends): 10,15,20,25.
Second set of numbers the user entered(subtrahends): 5,35. The calculation that is going to be made:
10 + 15 + 20 + 25 = 70 and 5 + 35 = 40. Final result = 70 - 40 = 30. The division works the same way, except that
the final numbers are divided, instead of subtracted''')
    print(f'''{yellow_text}Commands:
Addition[+]
Multiplication[x]
Subtraction[-]
Division[d]
When you finish typing the first set of numbers, enter "=" to type the second set of numbers and then,
enter "=" again to show the final result{reset_color}''')
    # print a blank line
    print()

    # makes a loop that never ends
    while True:
        # gets a command input
        command = input("Type an command(+, -, x, d): ")
        # checks if the user typed any of the specified commands, and if it did, the code below is executed
        # the \ is used to break a line, while complementing the code below, it's just for aesthetics
        if command == "+" or command == "addition" or command == "Addition" or command == "[+]" \
                or command == "Addition[+]" or command == "addition[+]" or command == "plus":
            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_numbers = get_number_input("Type a number to add it: ")
            # call the function that adds the numbers the user input and returns its values to a variable
            addition_result = add(list_of_Input_numbers)
            print(f"{green_text}The result of the addition is: {sea_green}{addition_result}{reset_color}")
        # if the statement above(the "if statement" at line 149") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line, while complementing the code below, it's just for aesthetics
        elif command == "-" or command == "subtraction" or command == "Subtraction" or command == "minus" \
                or command == "[-]" or command == "subtraction[-]" or command == "Subtraction[-]":
            # print a blank line
            print()
            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_numbers_minuends = get_number_input("Type the minuend(s) to be subtracted: ")
            list_of_Input_numbers_subtrahends = get_number_input("Type the subtrahend(s): ")
            # call the function that subtracts the numbers the user typed and returns the result to a variable
            subtraction_result = subtract(list_of_Input_numbers_minuends, list_of_Input_numbers_subtrahends)
            print(f"{green_text}The result of the subtraction is: {sea_green}{subtraction_result}{reset_color}")
        # if the statement above(the "elif statement" at line 159") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line, while complementing the code below, it's just for aesthetics
        elif command == "x" or command == "[x]" or command == "Multiplication" or command == "times" \
                or command == "multiplication[x]" or command == "Multiplication[x]":
            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_numbers = get_number_input("Type a number to multiply it: ")
            # call the function that multiplies the numbers the user typed and returns the result to a variable
            multiplication_result = multiply(list_of_Input_numbers)
            # print colored text
            print(f"{green_text}The result of the multiplication is: {sea_green}{multiplication_result}{reset_color}")
        # if the statement above(the "elif statement" at line 172") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line, while complementing the code below, it's just for aesthetics
        elif command == "d" or command == "/" or command == "D" or command == "[d]" or command == "division" \
                or command == "division[d]" or command == "Division[d]":
            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_dividends = get_number_input("Type the dividend(s)")
            list_of_Input_divisors = get_number_input("Type the divisor(s)")
            # call the function that divides the numbers the user typed and returns the result to a variable
            division_result = division(list_of_Input_dividends, list_of_Input_divisors)
            # print colored text
            print(f"{green_text}The result of the division is {sea_green}{division_result}{reset_color}")

        # print blank lines
        print()
        print()
        print("-=" * 20)
# The Code editor I used is Pycharm
# https://www.jetbrains.com/pycharm/
