def multiply_numbers(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide_numbers(a, b):
    """Returns the quotient of a divided by b. 
    Handles division by zero to prevent program crashes.
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# --- Example Usage ---

# Define two sample values
num1 = 20
num2 = 4

# Call the multiplication function
product = multiply_numbers(num1, num2)
print(f"Multiplication: {num1} * {num2} = {product}")

# Call the division function
quotient = divide_numbers(num1, num2)
print(f"Division: {num1} / {num2} = {quotient}")

# Example of handling division by zero safely
zero_division = divide_numbers(num1, 0)
print(f"Division by Zero Test: {zero_division}")
