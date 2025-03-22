def divide(a, b):
    if b == 0:
        return None
    return a // b

def exponent(a,b):
    return a**b

def remainder(a,b):
    if b == 0:
        return None
    return a%b

def summation(a,b):
    if a > b:
        return None
    return sum(range(a, b + 1))

while True:
    print("\nMain Menu:")
    print("[D] - DIVIDE")
    print("[E] - EXPONENTIATION")
    print("[R] - REMAINDER")
    print("[S] - SUMMATION")
    print("[L] - LEAVE")
    choice = input("Enter your choice: ")
        
    if choice in ['D', 'E', 'R', 'S']:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if choice == 'D':
            result = divide(a, b)
            print("Result: ", result if result is not None else "Invalid input")
        elif choice == 'E':
            result = exponent(a, b)
            print("Result: ", result)
        elif choice == 'R':
            result = remainder(a, b)
            print("Result: ", result if result is not None else "Invalid input")
        elif choice == 'S':
            result = summation(a, b)
            print("Result: ", result if result is not None else "Invalid input")
            
            
    elif choice == 'L':
        print("Exiting....")
        break
    else:
        print("Invalid input.Try again.")
    
    