# This is a sample Python script.
from termcolor import cprint

def Sum(*nums):
    global num
    nums = list(nums)
    # print(nums)
    count = 0
    result = 0
    for num in nums:
        count += len(num)
    else:
        for c in range(count):
            result += float(num[c])
    cprint(f"result = {result}", "green")


def get_number_input():
    global numbers
    numbers = []
    number = ""
    cprint("Type '=' to show the result of the addition", 'yellow')
    while True:

        number = str(input("Digite um número: "))
        if number == "=" or number == "==":
            break
        else:
            try:
                float(number)
            except ValueError:
                cprint("Invalid command!\nThis command didin't affect your addition", "red")
                cprint("-=" * 20, "blue")
            else:
                numbers.append(number)
    return numbers

if __name__ == '__main__':
    numbers = get_number_input()
    Sum(numbers)

