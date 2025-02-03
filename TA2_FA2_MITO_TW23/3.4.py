with open("TA2_FA2_MITO_TW23\students.txt", "r") as file:
        content = file.read()
        
if content.strip():
    print("\nReading Student Information:\n")
    print(content)
else:
    print("\nThe file is empty.")
