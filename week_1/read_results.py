import os

def read_results(file_name):
    if not os.path.exists(file_name):
        print(f"The file '{file_name}' does not exist.")
        return

    with open(file_name, "r") as file:
        content = file.read()

    print(f"Contents of '{file_name}':\n")
    print(content)

# Main program
file_name = "result.txt"
read_results(file_name)
