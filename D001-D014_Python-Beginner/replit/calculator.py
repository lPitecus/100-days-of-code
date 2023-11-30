def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}


num1 = float(input("First number: "))
for key in operations:
    print(key)
operation_symbol = input("\nChoose an operation from the options above: ")
num2 = float(input("\nSecond number: "))
first_result = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_result}")

continue_calculation = True
while continue_calculation:
    second_result = first_result
    choice = input(f"Type 'y' to continue calculating with {second_result}, or type 'n' to exit: ").lower()
    
    if choice == 'y':
        #repetir
        for key in operations:
            print(key)
        
        operation_symbol = input("\nChoose an operation from the options above: ")
        num3 = float(input("Next number: "))
        second_result = operations[operation_symbol](first_result, num3)
        print(f"{first_result} {operation_symbol} {num3} = {second_result}")
    
    elif choice == 'n':
        continue_calculation = False
        print("\n\nBye!")
