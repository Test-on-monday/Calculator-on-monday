def get_number_input():
    value = float(input())
    return value

print("=== Math Calculator ===")
print("Enter first number (num1 ≥ 0):")
num1 = get_number_input()

print("Enter second number (num2 > 0):")
num2 = get_number_input()

print("\nResults:")
print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Division: {num1} / {num2} = {divide(num1, num2)}")