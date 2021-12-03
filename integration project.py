"""__author__Walter Martinez Final integration project"""


# Addition Function
def add(number1, number2):
    number1 += number2
    return number1


# Subtraction Function
def substrac(number1, number2):
    number1 -= number2
    return number1


# Multiplication Function
def mult(number1, number2):
    number1 *= number2
    return number1


# Power Function
def pow(num1, num2):
    result = num1 ** num2
    return result


# Division Function
def div(num1, num2):
    result = num1 / num2
    wholeResult = num1 // num2
    remainder = num1 % num2
    return result, wholeResult, remainder


# String Multiplication Function
def stringmult(str1, str2):
    result = str1 * int(str2)
    return result


# String Concatenation
def concat(str1, str2):
    str1 += str2
    return str1


# Prime Numbers Sum Function
def primes(num1):
    sum = 0
    i = 1
    while i <= num1:
        if i > 1:
            counter = 0
            j = 2
            while j <= i:
                if i % j == 0:
                    counter += 1
                j += 1
            if counter == 1:
                sum += i
        i += 1
    return sum


def main():
    var = 'yes'
    print("Welcome to my final integration project!")
    while var.lower() == 'yes' or var.lower() == 'y':
        print("Select the operation: ")
        operations = ['Addition', 'Subtraction', 'Multiplication', 'Power',
                      'Division', 'String Multiplication',
                      'String Concatenation', 'Prime number summary']
        for i in range(len(operations)):
            print(operations[i] + ": " + str(i))
        try:
            option = int(input())
        except Exception:
            print("Error, input isn't a number. Closing...")
            break
        if option <= -1 or option > 7:
            print("Error, no operation selected")
        else:
            if (0 <= option <= 4) or option == 7:
                while True:
                    try:
                        num1 = int(input("Enter first number: "))
                        if option == 0:
                            # Addition Calculations
                            num2 = int(input("Enter second number: "))
                            print("Addition Operation")
                            result = add(num1, num2)
                            print("Result:" + str(result))
                            break
                        elif option == 1:
                            # Subtraction Calculations
                            num2 = int(input("Enter second number: "))
                            print("Subtraction Operation")
                            result = substrac(num1, num2)
                            print("Result:" + str(result))
                            break
                        elif option == 2:
                            # Multiplication Calculations
                            num2 = int(input("Enter second number: "))
                            print("Multiplication Operation")
                            result = mult(num1, num2)
                            print("Result:" + str(result))
                            break
                        elif option == 3:
                            # Power Calculations
                            num2 = int(input("Enter second number: "))
                            print("Power Operation")
                            result = pow(num1, num2)
                            print("Result:" + str(result))
                            break
                        elif option == 4:
                            # Division calculations
                            num2 = int(input("Enter second number: "))
                            print("Division Calculations")
                            result, whole, reminder = div(num1, num2)
                            print("Result with reminder:" + str(result))
                            print("Result without reminder: " + str(whole))
                            print("Reminder: " + str(reminder))
                            break
                        else:
                            # Prime Numbers Summary
                            print("Prime Numbers Summary")
                            result = primes(num1)
                            print("Result: " + str(result))
                            break
                    except Exception:
                        print("Error,try again")
                        continue
            elif option == 5 or option == 6:
                # string operations
                str1 = input("Enter first word:")
                if option == 5:
                    # String Multiplication
                    str2 = input("Enter a number:")
                    print("String Multiplication")
                    result = stringmult(str1, str2)
                    print("Result:" + result)
                elif option == 6:
                    # String Concatenation
                    str2 = input("Enter second word:")
                    print("String Concatenation")
                    result = concat(str1, str2)
                    print("Result:" + result)
            print(
                "Do you want to do another operation? yes(y)/no(any other "
                "text)")
            aux = input()
            if aux.lower() != 'yes' or aux.lower() != 'y':
                var = aux
                print("Thank you for using my program!")
                print("I hope you enjoy it!")


if __name__ == "__main__":
    main()
