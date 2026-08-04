num1 = int(input("Enter a num1:"))
num2 = int(input("Enter a num2:"))
operation = input("Enter the operation (+,-,*,/): ")

if operation == "+":
    print("the sum is", num1 + num2)
elif operation == "-":
    print("the difference is", num1 - num2)
elif operation == "*":
    print("the product is", num1 * num2)
elif operation == "/":
    print("the division is", num1 / num2)
else:
    print("invalid operation")
