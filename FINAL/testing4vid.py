#First Name
#Middle Name
#Last Name
#Birthday
#Gender
import tkinter

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window) #widget??
frame.pack() #layout manager daw pack for responsive

#Saving user info
user_info_frame = tkinter.LabelFrame(frame, text ="User Information")
user_info_frame.grid(row = 0, column = 0)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row = 0, column=0)

middle_name_label = tkinter.Label(user_info_frame, text="Middle Name")
middle_name_label.grid(row = 0, column=1)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row = 0, column=2)

first_name_entry = tkinter.Entry(user_info_frame)
middle_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

#2nd Row: Bday + Gender
bday_label = tkinter.Label(user_info_frame, text="Birthday (YYYY-MM-DD)")
bday_label.grid(row = 2, column=0)

gender_label = tkinter.Label(user_info_frame, text="Middle Name")
gender_label.grid(row = 2, column=1)

bday_entry = tkinter.Entry(user_info_frame)
gender_entry = tkinter.Entry(user_info_frame)
bday_entry.grid(row=3, column=0)
gender_entry.grid(row=3, column=1)


window.mainloop()