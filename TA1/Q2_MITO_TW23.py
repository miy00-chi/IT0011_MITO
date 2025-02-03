def sum_of_digits(string):
    total = 0
    for char in string:
        if char.isdigit():
            total += int(char)
    
    print(f"Sum of digits: {total}")

input_string = input("Enter a string containing digits: ")
sum_of_digits(input_string)