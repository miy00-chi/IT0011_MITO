Firstname = input("Enter First Name: ")
Lastname = input("Enter Last Name: ")
Age = input("Enter your age: ")

SlicedName = Firstname[:3]

print("Full Name: " + Firstname + " " + Lastname)
print("Sliced Name: ", SlicedName)
print("Hello, " + SlicedName + "! Welcome. You are " + Age + " years old")