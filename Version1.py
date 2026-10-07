def add_numbers(num1, num2):
    return num1 + num2
    
def subtract_numbers(num1, num2):
    return num1 - num2
    
def multiply_numbers(num1, num2):
    return num1 * num2
    
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Can't divide by 0."
    return num1/num2


    
    
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))

print("Operation?")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Choice:") 

if choice == "1":
    result = add_numbers(num1, num2)
    
if choice == "2":
    result = subtract_numbers_numbers(num1, num2)
    
if choice == "3":
    result = multiply_numbers(num1, num2)
    
if choice == "4":
    result = divide_numbers(num1, num2)

print("Result:", result)
    
