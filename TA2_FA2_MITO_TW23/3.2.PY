FirstName = input("Enter your First Name: ")
LastName = input("Enter your Last Name: ")

FullName = FirstName + " " + LastName

UpperName = FullName.upper()

LowerName = FullName.lower()

NameLength = len(FullName)

print("Full Name: ", FullName)
print("Full Name (Upper Case): ", UpperName)
print("Full Name (Lower Case): ", LowerName)
print("Length of Full Name: ", NameLength)