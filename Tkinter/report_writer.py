import pandas as pd
import datetime as dt
from tkinter import *
from tkinter import font, messagebox, filedialog



def report_writer():
    # Global variables
    global uni_df
    uni_df = pd.DataFrame()

    month_dict = {
        "January": 1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12
    }

    # FUNCTIONS
    def time_update():
        now = dt.datetime.now()
        # intro_label.config(text=f"Today: {now.month}-{now.day}-{now.year}  {now.hour}:{now.minute}")
        intro_label = Label(frame1, text=f"Today: {now.month}-{now.day}-{now.year}  {now.hour}:{now.minute}:{now.second}", bg="gray", font=font.Font(size=18), padx=5, pady=5)
        intro_label.grid(row=0, columnspan=3)
        root.after(1000, time_update)


    def new_df(dict): # adds all the entered info into a single df
        global uni_df
        date = str(dict[month.get()]) + "-" + str(day.get()) + "-" + str(year.get())
        if uni_df.shape[0] >= 20:
            messagebox.showwarning("Limit Reached", "Reached the maximum number of entries")
        else: 
            df_add = pd.DataFrame({"Date": [str(date)], "Hour": [int(hour.get())], "Minute": [int(minute.get())], "Description": [desc_Entry.get()]})
            uni_df = pd.concat([uni_df, df_add], axis=0)

            # Updates the history
            history_label.config(text=uni_df["Date"].head(20).to_string(index=False)) # This will be the date column of history
            hour_history.config(text=uni_df["Hour"].head(20).to_string(index=False)) 
            minute_history.config(text=uni_df["Minute"].head(20).to_string(index=False)) 
            desc_history.config(text=uni_df["Description"].head(20).to_string(index=False)) 

            # update scrollbar
            main_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))


    def save_file():
        filename = filedialog.asksaveasfile(title="Save CSV file", defaultextension=".csv", filetypes=[("csv files", "*.csv"), ("all files", "*.*")])
        uni_df.to_csv(filename)
            

    def confirm():
        confirmation = messagebox.askyesno("Confirmation", "Do you want to add this?")
        if confirmation: 
            if uni_df.empty:
                messagebox.showwarning("Warning", "No entries")
            
            else:
            # Read File
                pd.set_option("display.max_columns", None)
                filename = str(filedialog.askopenfilename(initialdir="/Home", title="Select Files", filetypes=[("csv files", "*.csv")])).replace("/", "\\")
                df = pd.read_csv(filename)
                if df.empty:
                    uni_df.to_csv(filename)
                else: 
                    col_names = [x for x in uni_df]
                    df_cols = [x for x in df.columns]
                    if df_cols == col_names:
                        save_new = messagebox.askyesno("Saving File", "Save this as a new file")
                        df_final = pd.concat([df, uni_df], axis=0, ignore_index=True)
                        if save_new:
                            file_new = filedialog.asksaveasfile(title="Save CSV file", defaultextension=".csv", filetypes=[("csv files", "*.csv"), ("all files", "*.*")])
                            df_final.to_csv(file_new)
                        else: 
                            df_final.to_csv(filename)
                    else: 
                        messagebox.showinfo("Header mismatched", "The column header of the file should be 'Date', 'Hour', 'Minute', 'Description'")

                    
            




    root = Tk()
    root.title("Monthly Report")
    root.columnconfigure(0, minsize=670)
    root.rowconfigure(0, weight=1)
    root.geometry("687x600")
    root.resizable(False, True)


    canvas = Canvas(root)
    canvas.grid(row=0, column=0, sticky="nsew")

    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Main Frame
    main_frame = LabelFrame(canvas, pady=20)
    canvas.create_window((0,0), window=main_frame, anchor="nw")



    # First Frame
    frame1 = LabelFrame(main_frame, text="Report Writer", padx=20, pady=50, height=520)
    frame1.grid(row=0, column=0, padx=30, pady=30, columnspan=2)

    # Intro w/ automatic date
    time_update()
    space_label = Label(frame1, text="", height=4) .grid(row=1) #Divider


    # Dropdown Menu Labels
    month_label = Label(frame1, text="Month", font=font.Font(size=14)).grid(row=2, column=0)
    day_label = Label(frame1, text="Day", font=font.Font(size=14)).grid(row=2, column=1)
    year_label = Label(frame1, text="Year", font=font.Font(size=14)).grid(row=2, column=2)
    desc_label = Label(frame1, text="Description", font=font.Font(size=14)).grid(row=7, column=1)
    hour_label = Label(frame1, text="Hours", font=font.Font(size=14)).grid(row=5, column=0)
    minute_label = Label(frame1, text="Minutes", font=font.Font(size=14)).grid(row=5, column=2)


    # Dropdown Menus
    month = StringVar()
    months_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months = OptionMenu(frame1, month, *months_names,)
    months.config(width=8, height=2)
    month.set(months_names[0])
    months.grid(row=3, column=0, padx=5, pady=5)

    day = IntVar() 
    days_num = [x for x in range(1, 32)]
    days = OptionMenu(frame1, day, *days_num)
    days.config(width=8, height=2)
    day.set(days_num[0])
    days.grid(row=3, column=1, padx=5, pady=5)

    year = IntVar()
    years_num = [x for x in range(2020, 2041)]
    years = OptionMenu(frame1, year, *years_num)
    years.config(width=8, height=2)
    year.set(years_num[0])
    years.grid(row=3, column=2, padx=5, pady=5)

    space_label = Label(frame1, text="", height=1)
    space_label.grid(row=4)

    hour = IntVar()
    hour_num = [x for x in range(0, 21)]
    hours = OptionMenu(frame1, hour, *hour_num)
    hours.config(width=8, height=2)
    hour.set(hour_num[0])
    hours.grid(row=6, column=0, padx=5, pady=5)

    minute = IntVar()
    minute_num = [x for x in range(0, 61, 5)]
    minutes = OptionMenu(frame1, minute, *minute_num)
    minutes.config(width=8, height=2)
    minute.set(minute_num[0])
    minutes.grid(row=6, column=2, padx=5, pady=5)

    # Description entry
    desc_Entry = Entry(frame1, width=50, font=("Helvetica", 15))
    desc_Entry.grid(row=8, column=0, columnspan=3)
    # Enter button
    enter_button = Button(frame1, text="Enter", command=lambda: new_df(month_dict))
    enter_button.grid(row=9, columnspan=3, pady=10)



    # Subframe shows all the inputs that we want to add
    history_frame = LabelFrame(main_frame, text="New Entries", padx=20, pady=20, height=500)

    history_label = Label(history_frame, text="No Records", font=font.Font(size=13), width=15)
    hour_history = Label(history_frame, text="", font=font.Font(size=13), width=5)
    minute_history = Label(history_frame, text="", font=font.Font(size=13), width=5)
    desc_history = Label(history_frame, text="", font=font.Font(size=13), width=33)

    # Placements
    history_frame.grid(row=1, column=0, padx=30, pady=30, columnspan=2)
    history_label.grid(row=11, column=0)
    hour_history.grid(row=11, column=1)
    minute_history.grid(row=11, column=2)
    desc_history.grid(row=11, column=3)


    # Confirmation to add all inputs in subframe
    confirm_button = Button(main_frame, text="Update", command=confirm, width=10, height=1)
    confirm_button.grid(row=4, column=0, pady=5)

    save_button = Button(main_frame, text="Save", command=save_file, width=10, height=1)
    save_button.grid(row=4, column=1, pady=5)

    main_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    root.mainloop()
    # REPORT WRITER CODE ENDS HERE




report_writer()

