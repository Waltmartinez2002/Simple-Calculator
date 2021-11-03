#Walter Martinez
#Sprint 2:standard conditional and iterative structures, the definition of functions, and parameter passing
#Functions
#Addition Function
def add(num1,num2):
    num1 += num2
    return num1
#Substraction Function
def substrac(num1,num2):
    num1 -= num2
    return num1
#Multiplication Function
def mult(num1,num2):
    num1 *= num2
    return num1
#Power Function
def pow(num1,num2):
    result = num1**num2
    return result
#Division Function
def div(num1,num2):
    result = num1/num2
    wholeresult = num1//num2
    reminder = num1%num2
    return result,wholeresult,reminder
#String Multiplication Function
def stringmult(str1,str2):
    result = str1*int(str2)
    return result
#String Concatenation
def concat(str1,str2):
    str1 += str2
    return str1
#Prime Numbers Sum Function
def primes(num1):
    sum = 0
    i = 1
    while i <= num1:
        if i > 1:
            counter = 0
            j = 2
            while j <= i:
                if i%j == 0:
                    counter+=1
                j+=1
            if counter == 1:
                sum += i
        i+=1
    return sum
                


var = 'yes'
print("Welcome to my sprint 2!")
while var == 'yes':
    print("Select the operation: ")
    operations = ['Addition','Substraction','Multiplication','Power','Division','String Multiplication', 'String Concatenation','Prime number summatory']
    for i in range(len(operations)):
        print(operations[i] + ": " + str(i))
    option=int(input())
    if option <= -1 or option >7:
        print("Error, no operation selected")
    else:
        if (option >= 0 and option <= 4) or option == 7:
            num1=int(input("Enter first number: "))
            if option == 0:
            #Addition Calculations
                num2=int(input("Enter second number: "))
                print("Addition Operation")
                result = add(num1,num2)
                print("Result:" + str(result))
            elif option == 1:
            #Substraction Calculations
                num2=int(input("Enter second number: "))
                print("Substraction Operation")
                result = substrac(num1,num2)
                print("Result:" + str(result))
            elif option == 2:
            #Multiplication Calculations
                num2=int(input("Enter second number: "))
                print("Multiplication Operation")
                result = mult(num1,num2)
                print("Result:" + str(result))
            elif option == 3:
                #Power Calculations
                num2=int(input("Enter second number: "))
                print("Power Operation")
                result = pow(num1,num2)
                print("Result:" + str(result))
            elif option == 4:
                #Division calculations
                num2=int(input("Enter second number: "))
                print("Division Calculations")
                result,whole,reminder = div(num1,num2)
                print("Result with reminder:" + str(result))
                print("Result without reminder: "+ str(whole))
                print("Reminder: "+str(reminder))
            else:
                #Prime Numbers Summatory
                print("Prime Numbers Summatory")
                result = primes(num1)
                print("Result: "+str(result))
        elif option == 5 or option == 6:              
            #string operations
            str1 = input("Enter first word:")
            if option == 5:
            #String Multiplication
                str2 = input("Enter a number:")
                print("String Multiplication")
                result = stringmult(str1,str2)
                print("Result:" + result)
            elif option == 6:
            #String Concatenation
                str2 = input("Enter second word:")
                print("String Concatenation")
                result = concat(str1,str2)
                print("Result:" + result)
        print("Do you want to do another operation? yes/no")
        aux = input()
        if aux == 'no':
            var = aux
            print("Thank you for using my program!")
            print("I hope you enjoy it!")

