# Writing functions to filter out water quality

def filtering(userInput):
    while True:
        try:
            value = float(input(userInput))
            return value  #return statement will "break" out of the function
        except ValueError:
            print("Invalid value, please try to enter another value.")

temp = filtering("Enter the Temperature: ")
turb = filtering("Enter the Turbidity: ")
tds = filtering("Enter the Total Disolved Solid: ")
disoxy = filtering("Enter the Dissolved Oxygen: ")
ph = filtering("Enter the pH level: ")

print(f"\nTemperature: {temp} °C")
print(f"Turbidity: {turb} NTU")
print(f"TDS: {tds} mg/l")
print(f"Dissolved Oxygen: {disoxy} mg/l")
print(f"pH level: {ph}")