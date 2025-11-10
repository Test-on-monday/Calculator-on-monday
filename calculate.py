def get_number_input():
   while True:
        try:
            value = float(input())  # No prompt text
        except ValueError:
            print("  Error: Please enter a valid numeric value!")
            continue

        if value < 0:
            print("  Error: Negative numbers are not allowed!")
            continue
    
        return value
def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

print("=== Math Calculator ===")
print("Enter first number (num1 ≥ 0):")
num1 = get_number_input()

print("Enter second number (num2 > 0):")
num2 = get_number_input()

print("\nResults:")
print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Division: {num1} / {num2} = {divide(num1, num2)}")