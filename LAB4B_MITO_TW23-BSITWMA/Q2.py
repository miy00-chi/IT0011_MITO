import csv

# Read the currency data from currency.csv
currencies = {}
with open('LAB4B_MITO_TW23-BSITWMA\currency.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader, None)  # Skip the header row
    print(f"Header: {header}")
    
    for row in reader:
        print(f"Reading row: {row}")
        if len(row) >= 3 and row[0].strip() and row[2].strip():
            currency = row[0].strip().upper()  # Currency code (e.g., AMD)
            try:
                rate = float(row[2].strip())  # Conversion rate
                currencies[currency] = rate
            except ValueError:
                print(f"Skipping invalid row: {row}")

# Show available currencies sorted alphabetically
print("\nAvailable currencies in file:")
for currency in sorted(currencies):
    print(f"- {currency}")

# User input for conversion
dollars = float(input("How much dollar do you have? "))
target_currency = input("What currency you want to have? ").strip().upper()
print(f"You entered: '{target_currency}'")

# Conversion and output
if target_currency in currencies:
    converted_amount = dollars * currencies[target_currency]
    print(f"\nDollar: {dollars} USD")
    print(f"{target_currency}: {converted_amount}")
else:
    print("Currency not found in the file.")
