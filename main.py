# This is a sample Python script.
from termcolor import cprint


# Function for addition of unlimited numbers
def Sum(*nums):
    global num
    nums = list(nums)
    # print(nums)
    count = 0
    result = 0
    # check each numbers in the list of inputs and count it's lenght
    for num in nums:
        count += len(num)
    else:
        # make an addition with each number in the list of inputs
        for c in range(count):
            result += float(num[c])
    cprint(f"result of the addition = {result}", "green")


# function for getting number inputs
def get_number_input():
    global numbers
    numbers = []
    cprint("Type '=' to show the addition result", 'yellow')
    while True:
        # number variable gets a string input
        number = str(input("Type a number: "))
        # break the input loop if "=" is typed
        if number == "=" or number == "==":
            break
        else:
            # check to see if a number was typed
            try:
                float(number)
            # if a there is ValueError error, the command is invalid and the input has letters or etc...
            except ValueError:
                cprint("Invalid number or command\nThe answer didn't affect your addition", "red")
                cprint("-=" * 20, "blue")
            # if everything goes ok, it adds the input to a number input list
            else:
                numbers.append(number)
    # returns a list with numbers
    return numbers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # call the function for getting unlimited number inputs
    numbers = get_number_input()
    # call the function to make an addition with the number inputs
    Sum(numbers)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
