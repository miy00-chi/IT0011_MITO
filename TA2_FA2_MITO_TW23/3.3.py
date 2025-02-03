LastName = input("Enter your Last Name: ")
FirstName = input("Enter your First Name: ")
Age = input("Enter your age: ")
ContactNumber = input("Enter Contact Number: ")
Course = input("Enter Course: ")

print("Last Name: ", LastName)
print("First Name: ", FirstName)
print("Age: ", Age)
print("Contact Numeber: ", ContactNumber)
print("Course: ", Course)

StudentInfo = "\nLast Name: " + LastName + "\nFirst Name: " + FirstName + "\nAge: " + Age + "\nContact Number: " + ContactNumber + "\nCourse: " + Course

with open("students.txt", "a") as file: 
    file.write(StudentInfo)
    
print("\nStudent information has been saved to 'students.txt' ")
