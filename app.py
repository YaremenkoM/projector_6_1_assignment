def main():
    print("This is simple calculator for two numbers.")
    print("Available operations: ")
    print("1 - Add")
    print("2 - Subtract")

    print("4 - Division")

    operation_type = input("Enter operation number: ")

    try:
        operation = int(operation_type)
        first_number = float(input("First number: "))
        second_number = float(input("Second number: "))
        result = 0
        if operation == 1:
            result = first_number + second_number
        elif operation == 2:
            result = first_number - second_number
        elif operation == 4:
            result = first_number / second_number
        else:
            print("There is no such an operation.")

        print("Result: " + str(result))
    except ValueError:
        print("Invalid input")


main()