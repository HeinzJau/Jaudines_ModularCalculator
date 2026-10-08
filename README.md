# Jaudines_ModularCalculator
This program works like a calculator, which asks the user to input two numbers and choose their operation from the following
- Addition
- Subtraction
- Multiplication
- Division


# REFLACTION
In this program, I created 4 functions. add_numbers, subtract_numbers, multiply_numbers, and divide_numbers. Each one has two parameters which are num1 and num2, which serve as placeholders for the user's number input. I passed the user-input variables num1 and num2 as actual arguments, and I stored the values returned by the functions in the variable result to display to the user. Structuring my calculator into functions rather than writing one long block of code is much better because it promotes reusability, improves overall code readability, simplifies testing, and makes maintenance easier since updates (like handling division by zero), only need to be made inside their specific function.
