def calculate(operation, x, y):
    if operation == "addition":
        return x + y
    elif operation == "subtraction":
        return x - y
    elif operation == "multiplication":
        return x * y
    elif operation == "division":
        return "undefined" if y == 0 else x / y
    else:
        return "Invalid operation"

# Main program loop
messages = ""
operation_list = ["addition", "subtraction", "multiplication", "division"]
while True:
    print("\nChoose an operation: addition, subtraction, multiplication, division")
    print("Type 'exit' to quit.")
    
    operation = input("Enter operation: ").strip().lower()
    

    if operation == "exit":
        break
    elif operation not in operation_list :
        print("Invalid operation. please try again.")
        continue
    
    try:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue
    
    result = calculate(operation, x, y)
    message = f"The result of {operation} is: {result}\n"
    print(message)
    messages += message

# Save all results to a file
with open("python-learning/result.txt", "a") as file:
    file.write(messages)
print("All results have been saved to result.txt.")
