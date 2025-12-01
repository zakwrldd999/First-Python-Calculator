# My first python calulator.


print("Welcome to my first python calulator!")


number1 = int(input("Enter your first number here:"))
number2 = int(input("Enter your second number here:"))
operation = input("Enter your choice of operation (+, -, *, /) ")

if operation == '+':
    print("The sum is:", number1 + number2)
elif operation == '-':
    print("The difference is:", number1 - number2)
elif operation == '*':
    print("The product is:", number1 * number2)
elif operation == '/':
    if number2 != 0:
        print("The quotient is:", number1 / number2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")


# Thank you for using my first python calulator.