records = []
current_file = ""

while True:
    print("\nMenu:")
    print("1. Add Record")
    print("2. Show All Students Record")
    print("3. Edit Record")
    print("4. Delete Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Save File")
    print("9. Save As File")
    print("10. Open File")
    print("11. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID (6 digits): ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added.")

    elif choice == "2":
        for record in records:
            print(record)

    elif choice == "3":
        student_id = input("Enter Student ID to edit: ")
        for i in range(len(records)):
            if records[i][0] == student_id:
                first_name = input("Enter New First Name: ")
                last_name = input("Enter New Last Name: ")
                class_standing = float(input("Enter New Class Standing Grade: "))
                major_exam = float(input("Enter New Major Exam Grade: "))
                records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("Record updated.")
                break
        else:
            print("Record not found.")

    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")
        for i in range(len(records)):
            if records[i][0] == student_id:
                records.pop(i)
                print("Record deleted.")
                break
        else:
            print("Record not found.")

    elif choice == "5":
        sorted_records = sorted(records, key=lambda x: x[1][1])
        for record in sorted_records:
            print(record)

    elif choice == "6":
        sorted_records = sorted(records, key=lambda x: (x[2] * 0.6) + (x[3] * 0.4), reverse=True)
        for record in sorted_records:
            print(record)

    elif choice == "7":
        student_id = input("Enter Student ID: ")
        for record in records:
            if record[0] == student_id:
                print(record)
                break
        else:
            print("Record not found.")

    elif choice == "8":
        if current_file:
            with open(current_file, "w") as file:
                for record in records:
                    file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
            print("File saved successfully.")
        else:
            print("No file opened. Use 'Save As' instead.")

    elif choice == "9":
        filename = input("Enter new file name: ")
        with open(filename, "w") as file:
            for record in records:
                file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")
        current_file = filename
        print("File saved successfully.")

    elif choice == "10":
        filename = input("Enter file name to open: ")
        try:
            with open(filename, "r") as file:
                records = []
                for line in file:
                    parts = line.strip().split(",")
                    student_id = parts[0]
                    first_name = parts[1]
                    last_name = parts[2]
                    class_standing = float(parts[3])
                    major_exam = float(parts[4])
                    records.append((student_id, (first_name, last_name), class_standing, major_exam))
                current_file = filename
                print("File opened successfully.")
        except FileNotFoundError:
            print("File not found.")

    elif choice == "11":
        break

    else:
        print("Invalid choice. Please try again.")
