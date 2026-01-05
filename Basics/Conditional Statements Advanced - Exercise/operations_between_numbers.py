num1 = int(input())
num2 = int(input())
operation = input()

calculate = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
}

if (operation == "/" or operation == "%") and num2 == 0:
    print(f"Cannot divide {num1} by zero")

else:
    result = calculate[operation](num1, num2)
    
    if operation == "/":
        result = f"{result:.2f}"
    
    
    print(f"{num1} {operation} {num2} = {result}", end="")
    
    if operation == "+" or operation == "-" or operation == "*":
        result_type = "even" if result % 2 == 0 else "odd"
        print(f" - {result_type}")


