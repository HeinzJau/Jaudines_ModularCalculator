def add_numbers(num1, num2):
    return num1 + num2
    
def subtract_numbers(num1, num2):
    return num1 - num2
    
def multiply_numbers(num1, num2):
    return num1 * num2
    
def divide_numbers(num1, num2):
    if num2 == 0: # Puts a restriction on dividing by 0 because it is not possible.
        return "Can't divide by 0."
    return num1/num2

# The line of code above defines the operations listed below.
    
    
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:")) # Asks the user to input their first and second number.

print("Operation?") # Asks the user which operation they would like to do
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Choice:") # Asks for the user's input

if choice == "1":
    result = add_numbers(num1, num2)
    
if choice == "2":
    result = subtract_numbers_numbers(num1, num2)
    
if choice == "3":
    result = multiply_numbers(num1, num2)
    
if choice == "4":
    result = divide_numbers(num1, num2)

print("Result:", result)

else:
    print("Unknown operation")
    
