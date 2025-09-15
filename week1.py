          # Simple calculator program
# Ask the user for input
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

#  calculate
result = eval(str(num1) + operation + str(num2))

# Show the answer
print(num1, operation, num2, "=", result)
