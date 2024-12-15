name = input("Enter your name: ")
message = f"Hello, {name}! Welcome to Python."

# Print the message
print(message)

# Save the message to a file
with open("greeting.txt", "w") as file:
    file.write(message)
print("Message saved to greeting.txt")
