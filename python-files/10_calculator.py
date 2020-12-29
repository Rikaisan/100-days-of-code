def validator(num=None, operator=None):
    if operator is not None:
        valid_operations = ["+", "-", "*", "/"]
        while operator not in valid_operations:
            operator = input("Not a valid operator, try again: ")
        if num is None:
            return operator
    while type(num) != float:
        try:
            num = float(num)
            if operator == "/" and num == 0:
                raise ZeroDivisionError
            return num
        except ValueError:
            num = input("Not a valid number, type a number: ")
        except ZeroDivisionError:
            num = input("Can not divide by zero, type another number: ")


def run_operation(operation, num1, num2):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2
    }
    return operations.get(operation)


def continue_calculating(number):
    keep_going = input("Do you want to continue calculating? (q to quit, else to keep going)\n").lower().strip()
    if keep_going and keep_going[0] == 'q':
        exit()
    ask(number)


def ask(num1):
    operation = input("Please choose an operation [+, -, *, /]: ").strip()
    operation = validator(operator=operation)
    number2 = input("Type a number: ")
    number2 = validator(number2, operation)
    result = run_operation(operation, num1, number2)
    print(f"Result: {result}")

    continue_calculating(result)


number1 = input("Type a number: ")
number1 = validator(number1)
ask(number1)
