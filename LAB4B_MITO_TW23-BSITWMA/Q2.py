import csv

currencies = {}
with open('LAB4B_MITO_TW23-BSITWMA\currency.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader, None)  
    print(f"Header: {header}")
    
    for row in reader:
        print(f"Reading row: {row}")
        if len(row) >= 3 and row[0].strip() and row[2].strip():
            currency = row[0].strip().upper()  
            try:
                rate = float(row[2].strip())  
                currencies[currency] = rate
            except ValueError:
                print(f"Skipping invalid row: {row}")

print("\nAvailable currencies in file:")
for currency in sorted(currencies):
    print(f"- {currency}")

dollars = float(input("How much dollar do you have? "))
target_currency = input("What currency you want to have? ").strip().upper()
print(f"You entered: '{target_currency}'")

if target_currency in currencies:
    converted_amount = dollars * currencies[target_currency]
    print(f"\nDollar: {dollars} USD")
    print(f"{target_currency}: {converted_amount}")
else:
    print("Currency not found in the file.")
