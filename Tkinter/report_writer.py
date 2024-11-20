import pandas as pd
import time
import datetime as dt
from tkinter import *
from tkinter import font, messagebox

root = Tk()
root.title("Monthly Report")
# root.geometry("410x600")

# Read File
pd.set_option("display.max_columns", None)
df = pd.read_csv(r"C:\Users\samil\Downloads\report_2024.csv")

# df_label = Label(root, text=df.sample(10), width=50).grid(row=2)

# First Frame
frame1 = LabelFrame(root, text="Report Writer", padx=20, pady=20, width=1000)
frame1.grid(row=0, column=0, padx=30, pady=30)
# frame1.grid_columnconfigure(0, minsize=300)
# frame1.grid_rowconfigure(0, minsize=150)

# date
now = dt.datetime.now()
# intro
intro_label = Label(frame1, text=f"Today: {now.month}-{now.day}-{now.year}  {now.hour}:{now.minute}", bg="gray", font=font.Font(size=18), padx=5, pady=5)
intro_label.grid(row=0, columnspan=3)

space_label = Label(frame1, text="", height=4)
space_label.grid(row=1)



# Functions
# def show():
#     showlabel = Label(root, text=month.get()).pack()
global uni_df
uni_df = pd.DataFrame()

def new_df(): # adds all the entered info into a single df
    description = desc_Entry.get()
    record = [month.get(), day.get(), year.get(), description]
    df_add = pd.DataFrame(record, columns=["Date", "Hours", "Minutes", "Desc"])
    uni_df = pd.concat([uni_df, df_add], axis=0)



def confirm():
    confirmation = messagebox.askyesno("COnfirmation", "Do you want to add this?")


def update():
    return





# Dropdown Menu Labels
month_label = Label(frame1, text="Month", font=font.Font(size=14)).grid(row=2, column=0)
day_label = Label(frame1, text="Day", font=font.Font(size=14)).grid(row=2, column=1)
year_label = Label(frame1, text="Year", font=font.Font(size=14)).grid(row=2, column=2)
desc_label = Label(frame1, text="Description", font=font.Font(size=14)).grid(row=5, column=1)




# Dropdown Menus
month = StringVar()
months_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = OptionMenu(frame1, month, *months_names,)
months.config(width=8, height=2)
month.set(months_names[0])
months.grid(row=3, column=0, padx=5, pady=5)

day = IntVar() 
days_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
days = OptionMenu(frame1, day, *days_num)
days.config(width=8, height=2)
day.set(days_num[0])
days.grid(row=3, column=1, padx=5, pady=5)

year = IntVar()
years_num = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040]
years = OptionMenu(frame1, year, *years_num)
years.config(width=8, height=2)
year.set(years_num[0])
years.grid(row=3, column=2, padx=5, pady=5)

space_label = Label(frame1, text="", height=1)
space_label.grid(row=4)

desc_Entry = Entry(frame1, width=50, font=("Helvetica", 15))
desc_Entry.grid(row=6, column=0, columnspan=3)

enter_button = Button(frame1, text="Enter", command=new_df).grid(row=7, columnspan=3, pady=10)



# Subframe shows all the inputs that we want to add
history_frame = LabelFrame(root, text="History", padx=20, pady=20, width=1000).grid(row=9, column=0, padx=30, pady=30)
update_button = Button(history_frame, text="Update", command=update).grid(row=10)
history_label = Label(history_frame, text=uni_df.head(50), width=60).grid(row=11)

# # Confirmation to add all inputs in subframe
# confirm_button = Button(frame1, text="Enter", command=confirm)


# # Divider Frame
# frame_divide = LabelFrame(root, text="").pack()
# label_divide = Label(frame_divide, text="\n\n").pack()



# frame2 = LabelFrame(root, text="Report Viewer")
# frame2.pack()

# df_label = Label(frame2, text=df.sample(10), width=50).pack()








root.mainloop()
