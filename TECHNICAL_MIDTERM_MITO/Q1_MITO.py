file = open('TECHNICAL_MIDTERM_MITO\\numbers.txt', 'r')
lines = file.readlines()
file.close()

line_number = 1
for line in lines:
    numbers = line.strip().split(',')  
    total = 0
    
    for num in numbers:
        total += int(num)
    
    if str(total) == str(total)[::-1]:
        result = "Palindrome"
    else:
        result = "Not a palindrome"

    print("Line", line_number, ":", ','.join(numbers), "(sum", total, ") -", result)
    line_number += 1