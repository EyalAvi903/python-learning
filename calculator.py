def calculate_and_save(operation, op_symbol):
    print(f"Please input two numbers for {operation}")
    x = int(input("Enter x - "))
    y = int(input("Enter y - "))

    if operation == "division" and y == 0:
        result = "undefined (cannot divide by zero)"
    else:
        result = eval(f"{x} {op_symbol} {y}")
    
    message = f"The result of {operation} is: {result}.\n"
    print(message)
    return message

# Perform all operations
message1 = calculate_and_save("addition", "+")
message2 = calculate_and_save("subtraction", "-")
message3 = calculate_and_save("multiplication", "*")
message4 = calculate_and_save("division", "/")

# Save all results to a file
messages = message1 + message2 + message3 + message4
with open("python-learning/result.txt", "w") as file:
    file.write(messages)

print("Results saved to result.txt")
