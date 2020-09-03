# This is a sample Python script.
from termcolor import cprint


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
    cprint(f"resultado = {result}", "green")


def get_number_input():
    global numbers
    numbers = []
    number = ""
    cprint("Digite '=' para mostrar o resultado da adição", 'yellow')
    while True:

        number = str(input("Digite um número: "))
        if number == "=" or number == "==":
            break
        else:
            try:
                float(number)
            except ValueError:
                cprint("Número ou comando inválido\nA resposta não foi contada", "red")
                cprint("-=" * 20, "blue")
            else:
                numbers.append(number)
    return numbers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = get_number_input()
    Sum(numbers)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
