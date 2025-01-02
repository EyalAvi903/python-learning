def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\nTemperature Converter")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("Type 'exit' to quit.")
    
    choice = input("Choose an option: ").strip().lower()
    if choice == "exit":
        break
    elif choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Invalid choice. Please try again.")
