# Basic Calculator Program
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Enter an operation (+'-,*,/):")
#Perform the operation and print the result
if operator == '+':
    result = num1 +num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}") 
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}") 
elif operator == '/':
    if num2 !=0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division  by zero is not allowed.") 
else:print("Invalid operator. Please enter +,-,*,or /.")            