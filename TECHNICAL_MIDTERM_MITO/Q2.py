date_input = input("Enter the date (mm/dd/yyyy): ")

month = date_input[0:2]
day = date_input[3:5]
year = date_input[6:]

if month == "01":
    month_name = "January"
elif month == "02":
    month_name = "February"
elif month == "03":
    month_name = "March"
elif month == "04":
    month_name = "April"
elif month == "05":
    month_name = "May"
elif month == "06":
    month_name = "June"
elif month == "07":
    month_name = "July"
elif month == "08":
    month_name = "August"
elif month == "09":
    month_name = "September"
elif month == "10":
    month_name = "October"
elif month == "11":
    month_name = "November"
elif month == "12":
    month_name = "December"
else:
    month_name = "Unknown"

day_number = int(day)

print("Date Output: " + month_name + " " + str(day_number) + ", " + year)
