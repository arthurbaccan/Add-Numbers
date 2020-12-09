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


# Function for the addition of unlimited numbers
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


# Function for the subtraction of unlimited numbers
def subtract(numbers: list):
    # assignment of variables that are going to be used later
    result = 0
    # "First_time" variable is used to check if the first loop in the for loop is being executed.
    first_time = True
    # stores the length of "nums" list in a variable called count
    count = len(numbers)
    # subtracts each number in the "nums" list(that has the inputs from the user)
    for c in range(count - 1):
        if first_time:
            result = float(numbers[c]) - int(numbers[c + 1])
            first_time = False
        else:
            result -= float(numbers[c + 1])
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
            result *= float(nums[c + 1])
    # returns the "result" variable
    return result


# function for the division of unlimited numbers
def division(dividends: list, divisors: list):
    # assignment of the variables that are going to be used later
    sum_dividends = 0.0
    sum_divisors = 0.0
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
    result = float(sum_dividends) / float(sum_divisors)
    # returns the "result" variable
    return result


# function for the addition of time with unlimited numbers
def add_time(hours: list, minutes: list, seconds: list):
    # assignment of the variables that are going to be used later
    total_seconds = 0
    total_minutes = 0
    total_hours = 0
    # checks if there is anything in the "seconds" list, and execute the code below or not
    if seconds:
        # adds every second in the "seconds" list
        for c in range(len(seconds)):
            # "total_seconds" variable gets the total number of seconds in the "seconds" list
            total_seconds += int(seconds[c])

        if total_seconds >= 60:
            total_minutes += total_seconds // 60  # Exchange seconds for minutes
            total_seconds -= total_seconds // 60 * 60  # Subtracts the number of seconds that were exchanged for minutes

    # checks if there is anything in the "minutes" list executes the code below or not
    if minutes:
        # adds every minute in the "minutes" list
        for c in range(len(minutes)):
            # "total_minutes" variable gets the total number of minutes in the "minutes" list
            total_minutes += int(minutes[c])

        if total_minutes >= 60:
            total_hours += total_minutes // 60  # Exchanges minutes for hours
            total_minutes -= total_minutes // 60 * 60  # Subtracts the number of minutes that were exchanged for hours

    # checks if there is anything in the "hours" list, and execute the code below or not
    if hours:
        # adds every hour in the "hour" list
        for c in range(len(hours)):
            # "total_hours" variable gets the total number of seconds in the "seconds" list
            total_hours += int(hours[c])
    # returns a phrase with the addition results
    # The pattern is: hours:minutes:seconds. Ex: 12:34:56
    return f'{total_hours}:{total_minutes}:{total_seconds}'


# function for the subtraction of time with unlimited numbers
def subtract_time(list_of_hours, list_of_minutes, list_of_seconds, list_of_hours2, list_of_minutes2, list_of_seconds2):
    # assignment of the variables that are going to be used later
    # The addition of the hours, minutes, seconds is made by the "add_time" function and its result is stored in the
    # time_1, time_2 variables
    time_1 = add_time(list_of_hours, list_of_minutes, list_of_seconds)
    time_2 = add_time(list_of_hours2, list_of_minutes2, list_of_seconds2)
    # The result of the addition of time is a string with this pattern: hours:minutes:seconds
    # example: 12:23:45.The hours, minutes, seconds are separated and stored into variables
    time_1hour, time_1minute, time_1second = time_1.split(':')
    time_2hour, time_2minute, time_2second = time_2.split(':')
    # the variables are converted from string(text) to int(numbers) and stored in lists
    time_1 = int(time_1hour), int(time_1minute), int(time_1second)
    time_2 = int(time_2hour), int(time_2minute), int(time_2second)
    time_1 = list(time_1)
    time_2 = list(time_2)

    # the minutes, hours, seconds are subtracted
    subtraction_hours = time_1[0] - time_2[0]
    subtraction_minutes = time_1[1] - time_2[1]
    subtraction_seconds = time_1[2] - time_2[2]
    # if the result of the subtraction is negative, It converts minutes to seconds or hours to minutes because
    # there is no negative time(all those calculations are needed because time(hours, minutes, seconds) use the base 60
    # instead of 10. Ex(base 60): 60 seconds = 1 minutes. Ex(base 10): 10 ones = 1 ten
    if subtraction_seconds < 0:
        subtraction_seconds *= -1  # makes the number positive so it gets more intuitive and the division works well.
    # some logic, so the correct number of seconds get displayed
        if subtraction_seconds <= 60:

            subtraction_seconds *= -1  # Makes the number negative(original state) so it gets more intuitive

            subtraction_seconds += 60
            subtraction_minutes -= 1
        else:
            subtraction_minutes -= subtraction_seconds // 60
            subtraction_seconds -= subtraction_seconds // 60 * 60

            if subtraction_seconds <= 60:
                subtraction_seconds *= -1
                subtraction_minutes -= 1
                subtraction_seconds += 60

    if subtraction_minutes < 0:
        subtraction_minutes *= -1   # makes the number positive so it gets more intuitive and the division works well
    # some logic, so the correct number of minutes get displayed
        if subtraction_minutes <= 60:

            subtraction_minutes *= -1  # Makes the number negative(original state)

            subtraction_minutes += 60
            subtraction_hours -= 1

        else:
            subtraction_hours -= subtraction_minutes // 60
            subtraction_minutes -= subtraction_minutes // 60 * 60

            if subtraction_minutes <= 60:
                subtraction_minutes *= -1
                subtraction_hours -= 1
                subtraction_minutes += 60
    # returns the time(hours, minutes, seconds) subtraction result
    return f'{subtraction_hours}:{subtraction_minutes}:{subtraction_seconds}'


# function that prints instructions
def print_instructions():
    # instructions:
    print(f'''{gray_text}Instructions: 
    Type a command(from the command list below) to chose a mode,
    and start doing calculations with unlimited numbers. 
    Don't forget to press "enter" after you type a number.
    When you finish typing the first set of numbers, enter "=" to type the next set of numbers and when you finish,
    enter "=" to show the final result''')
    print('''Division works this way: The first set of numbers you enter(dividends) will be subtracted from the
    second set of numbers you type(divisors). Example: First set of numbers the user entered(dividends): 10,15,20,25.
    Second set of numbers the user entered(divisors): 5,35. The calculation that is going to be made:
    10 + 15 + 20 + 25 = 70 and 5 + 35 = 40. Final result = 70 ÷ 40 = 1.75
    Subtraction with time works the same way, example: hours(minuends) + minutes(minuends) + seconds(minuends) - hours
    (subtrahends) + minutes(subtrahends) + seconds(subtrahends)
    Test it and you'll understand better''')
    print(f'''{yellow_text}Commands:
    instruction[i]
    Addition[+]
    Addition of time[t+]
    Multiplication[x]
    Subtraction[-]
    Division[d]
    Subtraction of time[t-]
    When you finish typing the first set of numbers(press 'enter' after typing each number),
    enter "=" to type the next set of numbers and then, enter "=" again to show the final result{reset_color}''')
    # prints a blank line
    print()


# function for getting number inputs from the user
# the "message" parameter is going to be displayed to the user
def get_number_input(message="Type a number"):
    # make List_of_Input_numbers a global variable, so it can be used in all indentations of the function
    global list_of_Input_numbers
    list_of_Input_numbers = []
    # while loop for getting an infinite amount of inputs
    while True:
        # variable called "input_number" gets a string input from the user
        input_number = str(input(message))
        # "if statement" breaks the input loop if "=" is typed
        if input_number == "=" or input_number == "==":
            break
        else:
            # Tries to run the code below without getting errors
            try:
                float(input_number)
            # if a there is ValueError error, the user typed something else than numbers.
            # and the program deal with it.
            except ValueError:
                print(f"{red_text}Invalid number or command\nThe answer didn't affect your calculation ")
                print(f"{blue_text}-={reset_color}" * 20, )
            # if everything goes ok(without errors), it adds the user input to a list called "List_of_Input_numbers"
            else:
                list_of_Input_numbers.append(input_number)
    # returns a list with numbers that the user input
    return list_of_Input_numbers


if __name__ == '__main__':
    # prints colored instructions
    print_instructions()
    print("-=" * 20)
    # makes a loop that never ends
    while True:

        # gets a command input
        command = input("Type an command(+, -, i, ...): ")
        # checks if the user typed any of the specified commands, and if it did, the code below is executed
        # the \ is used to break a line while complementing the code below, it's just for aesthetics
        if command == "+" or command == "addition" or command == "Addition" or command == "[+]" \
                or command == "Addition[+]" or command == "addition[+]" or command == "plus":

            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_numbers = get_number_input("Type a number to add it: ")
            # call the function that adds the numbers the user input and returns its values to a variable
            addition_result = add(list_of_Input_numbers)
            print(f"{green_text}The result of the addition is: {sea_green}{addition_result}{reset_color}")


        # if the statement above(the "if statement" at line 262") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line while complementing the code below, it's just for aesthetics
        elif command == "-" or command == "subtraction" or command == "Subtraction" or command == "minus" \
                or command == "[-]" or command == "subtraction[-]" or command == "Subtraction[-]":

            # print a blank line
            print()
            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_numbers = get_number_input('Type numbers to subtract them: ')
            # call the function that subtracts the numbers the user typed and returns the result to a variable
            subtraction_result = subtract(list_of_Input_numbers)
            print(f"{green_text}The result of the subtraction is: {sea_green}{subtraction_result}{reset_color}")


        # if the statement above(the "elif statement" at line 275") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line while complementing the code below, it's just for aesthetics
        elif command == "x" or command == "[x]" or command == "Multiplication" or command == "times" \
                or command == "multiplication[x]" or command == "Multiplication[x]":

            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_numbers = get_number_input("Type a number to multiply it: ")
            # call the function that multiplies the numbers the user typed and returns the result to a variable
            multiplication_result = multiply(list_of_Input_numbers)
            # print colored text
            print(f"{green_text}The result of the multiplication is: {sea_green}{multiplication_result}{reset_color}")


        # if the statement above(the "elif statement" at line 290") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line while complementing the code below, it's just for aesthetics
        elif command == "d" or command == "/" or command == "D" or command == "[d]" or command == "division" \
                or command == "division[d]" or command == "Division[d]":

            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_Input_dividends = get_number_input("Type the dividend(s): ")
            list_of_Input_divisors = get_number_input("Type the divisor(s): ")
            # Try to run the function getting without errors
            try:
                # call the function that divides the numbers the user typed and returns the result to a variable
                division_result = division(list_of_Input_dividends, list_of_Input_divisors)
            # If there is a ZeroDivisionError, it runs the code below
            except ZeroDivisionError:
                print(f"{sea_green}The result of a division by zero is infinite{reset_color}")
            # If everything goes well, it show th result
            else:
                # print colored text
                print(f"{green_text}The result of the division is {sea_green}{division_result}{reset_color}")


        # if the statement above(the "elif statement" at line 304") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line while complementing the code below, it's just for aesthetics
        elif command == 't+' or command == 't' or command == 'Addition of time[t+]' or command == '[t+]' or command \
                == 'Addition[t+]' or command == 'Addition of time' or command == '+t' or command == '[+t]' \
                or command == 'time+' or command == '+time' or command == 'time addition' or command == 'plus time':

            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_hours = get_number_input("Hours: ")
            list_of_minutes = get_number_input("Minutes: ")
            list_of_seconds = get_number_input("Seconds: ")
            try:
                # call the function that does additions with time and returns the result to a variable
                time_addition_result = add_time(list_of_hours, list_of_minutes, list_of_seconds)
            except ValueError:
                print(f"{red_text}Don't type decimal numbers in this mode{reset_color}")
            else:
                # print colored text
                print(f'{sea_green}The result of the addition(hours, minutes, seconds) is {time_addition_result}'
                      f'{reset_color}')  # line break for aesthetics. This doesn't affect the printed message


        # if the statement above(the "elif statement" at line 302") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line while complementing the code below, it's just for aesthetics
        elif command == 'i' or command == 'instruction[i]' or command == '[i]' or command == 'I' or command == '[I]' \
                or command == 'Instructions[i]' or command == 'instructions' or command == 'Instructions':

            # calls the function that prints instructions
            print_instructions()


        # if the statement above(the "elif statement" at line 348") is not executed it checks if the user typed
        # any of the specified commands, and the code below is executed or not
        # the \ is used to break a line while complementing the code below, it's just for aesthetics
        elif command == 't-' or command == 'Subtraction of time[t-]' or command == '[t-]' or command \
                == 'Subtraction[t-]' or command == 'Subtraction of time' or command == '-t' or command == '[-t]' \
                or command == 'time-' or command == '-time' or command == 'time subtraction' or command == 'minus time':

            # Gets a list of the numbers that the user typed and assign them to a variable
            list_of_hours = get_number_input("Hours(minuends): ")
            list_of_minutes = get_number_input("Minutes(minuends): ")
            list_of_seconds = get_number_input("Seconds(minuends): ")
            list_of_hours2 = get_number_input("Hours(subtrahends): ")
            list_of_minutes2 = get_number_input("Minutes(subtrahends): ")
            list_of_seconds2 = get_number_input("Seconds(subtrahends): ")
            try:
                # call the function that does subtractions with time and returns the result to a variable
                time_subtraction_result = subtract_time(list_of_hours, list_of_minutes, list_of_seconds, list_of_hours2,
                                                        list_of_minutes2, list_of_seconds2)  # line break for aesthetics

            except ValueError:
                print(f"{red_text}Don't type decimal numbers in this mode{reset_color}")
            else:
                # print colored text
                print(f'{sea_green}The result of the subtraction(hours, minutes, seconds) is {time_subtraction_result}'
                      f'{reset_color}')  # line break for aesthetics. This doesn't affect the printed message
        else:
            pass

        # print blank lines
        print()
        print()
        print("-=" * 20)
# The Code editor I used is Pycharm
# https://www.jetbrains.com/pycharm/
