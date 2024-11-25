import pandas as pd
import datetime as dt
from tkinter import *
from tkinter import font, messagebox, filedialog
import datetime
from tkcalendar import Calendar


def report_writer():
    try: 
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
            intro_label = Label(frame1, text=f"Today: {now.month}-{now.day}-{now.year}  {now.hour}:{now.minute}:{now.second}", bg="gray", font=font.Font(size=18), padx=5, pady=5, width=40)
            intro_label.grid(row=0, columnspan=5, sticky="ew")
            root.after(1000, time_update)


        def description_maker():
            description = [var1.get(), var2.get(), var3.get(), var4.get()]
            new_desc = ""
            for x in description:
                if x != "":
                    new_desc = new_desc + ":" + str(x)
                    print("inside")
                else:
                    pass
            return new_desc[1:]


        def new_df(dict): # adds all the entered info into a single df
            global uni_df
            date = str(calendar.get_date())
            description = description_maker()
            if uni_df.shape[0] >= 20:
                messagebox.showwarning("Limit Reached", "Reached the maximum number of entries")
            else: 
                df_add = pd.DataFrame({"Date": [date], "Hour": [int(hour.get())], "Minute": [int(minute.get())], "Description": [description]})
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
            if uni_df.empty:
                messagebox.showwarning("Empty File", "File empty (No entries)")
            else: 
                filename = filedialog.asksaveasfile(title="Save CSV file", defaultextension=".csv", filetypes=[("csv files", "*.csv")])
                uni_df.to_csv(filename)
                messagebox.showinfo("Saving File", "File successfully saved!")
                

        def confirm():
            global uni_df
            confirmation = messagebox.askyesno("Confirmation", "Do you want to add this?")
            if confirmation: 
                if uni_df.empty:
                    messagebox.showwarning("Warning", "No entries")
                
                else:
                # Read File
                    try: 
                        filename = str(filedialog.askopenfilename(initialdir="/Home", title="Select Files", filetypes=[("csv files", "*.csv")])).replace("/", "\\")
                        df = pd.read_csv(filename)[["Date", "Hour", "Minute", "Description"]]
                        if df.empty: # Handling empty csv file
                            if filename:
                                uni_df.to_csv(filename)
                            else: 
                                messagebox.showinfo("Canceled", "File Saving Canceled")

                        else: 
                            print(uni_df.columns)
                            print(df.columns)
                            matched = (df.columns == uni_df.columns).all()

                            if matched: # Handling unmatched columns
                                save_new = messagebox.askyesno("Save or Modify File", "Save this as a new file?")
                                df_final = pd.concat([df, uni_df], axis=0, ignore_index=True)
                                if save_new:
                                    file_new = filedialog.asksaveasfile(title="Save CSV file", defaultextension=".csv", filetypes=[("csv files", "*.csv")])
                                    df_final.to_csv(file_new)
                                    messagebox.showinfo("File Saved", "New File Saved")
                                else: 
                                    df_final.to_csv(filename)
                                    messagebox.showinfo("File Saved", "Edited File Saved")
                            else: 
                                messagebox.showinfo("Header mismatched", "The column header of the file should be 'Date', 'Hour', 'Minute', 'Description'")
                    except Exception: 
                        messagebox.showinfo("Canceled", "File Saving Canceled")

        def quit():
            quit_val = messagebox.askokcancel("Exit", "Do you want to exit?")
            if quit_val:
                root.destroy()
                

        root = Tk()
        root.title("Monthly Report")
        root.iconbitmap(r"C:\Users\samil\Downloads\report_document_finance_business_analysis_analytics_chart_icon_188615.ico")
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
        main_frame = LabelFrame(canvas, pady=20, bg="gray")
        canvas.create_window((0,0), window=main_frame, anchor="nw")

        # First Frame
        frame1 = LabelFrame(main_frame, text="Report Writer", padx=20, pady=50, height=520)
        frame1.grid(row=0, column=0, padx=30, pady=30, columnspan=3)

        # Intro w/ automatic date
        time_update()
        space_label = Label(frame1, text="", height=4).grid(row=1) #Divider


        calendar = Calendar(frame1, selectmode="day", date_pattern="yyyy-m-d", weekheader=True, mindate=datetime.date(2020, 1, 1), maxdate=datetime.date(2050, 12, 31))
        calendar.grid(row=2, column=0, columnspan=5, sticky="ew")


        space_label = Label(frame1, text="", height=1)
        space_label.grid(row=3, sticky="ew")

        hour_label = Label(frame1, text="Hours", font=font.Font(size=14)).grid(row=4, column=0)
        hour = IntVar()
        hour_num = [x for x in range(0, 25)]
        hours = OptionMenu(frame1, hour, *hour_num)
        hours.config(width=8, height=2)
        hour.set(hour_num[0])
        hours.grid(row=4, column=1, padx=5, pady=5)
        
        minute_label = Label(frame1, text="Minutes", font=font.Font(size=14)).grid(row=4, column=3)
        minute = IntVar()
        minute_num = [x for x in range(0, 61, 5)]
        minutes = OptionMenu(frame1, minute, *minute_num)
        minutes.config(width=8, height=2)
        minute.set(minute_num[0])
        minutes.grid(row=4, column=4, padx=5, pady=5)

        space_label = Label(frame1, text="", height=1)
        space_label.grid(row=5)

        # Description checklist
        
        checklist = [
                ("House to house", "house to house"), ("Cart", "cart"), ("Study", "study"), ("Return Visit", "return visit")
            ]
        
        var1, var2, var3, var4 = [StringVar(), StringVar(), StringVar(), StringVar()]

        house = Checkbutton(frame1, text=checklist[0][0], variable=var1, onvalue=checklist[0][1], offvalue="")
        cart = Checkbutton(frame1, text=checklist[1][0], variable=var2, onvalue=checklist[1][1], offvalue="")
        study = Checkbutton(frame1, text=checklist[2][0], variable=var3, onvalue=checklist[2][1], offvalue="")
        rv = Checkbutton(frame1, text=checklist[3][0], variable=var4, onvalue=checklist[3][1], offvalue="")

        house.grid(row=6, column=0)
        cart.grid(row=6, column=1)
        study.grid(row=6, column=3)
        rv.grid(row=6, column=4)
        



        
        # Enter button
        enter_button = Button(frame1, text="Enter", command=lambda: new_df(month_dict))
        enter_button.grid(row=7, columnspan=5, pady=10)



        # Subframe shows all the inputs that we want to add
        history_frame = LabelFrame(main_frame, text="New Entries", padx=20, pady=20, height=500)

        history_label = Label(history_frame, text="No Records", font=font.Font(size=13), width=15)
        hour_history = Label(history_frame, text="", font=font.Font(size=13), width=5)
        minute_history = Label(history_frame, text="", font=font.Font(size=13), width=5)
        desc_history = Label(history_frame, text="", font=font.Font(size=13), width=33)

        # Placements
        history_frame.grid(row=1, column=0, padx=30, pady=30, columnspan=3)
        history_label.grid(row=2, column=0)
        hour_history.grid(row=2, column=1)
        minute_history.grid(row=2, column=2)
        desc_history.grid(row=2, column=3)


        # Confirmation to add all inputs in subframe
        confirm_button = Button(main_frame, text="Update", command=confirm, width=10, height=1)
        confirm_button.grid(row=3, column=0, pady=5)

        save_button = Button(main_frame, text="Save", command=save_file, width=10, height=1)
        save_button.grid(row=3, column=2, pady=5)

        exit_button = Button(root, text="Exit", command=quit, width=10, height=1)
        exit_button.grid(row=4, pady=5)

        main_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        root.mainloop()
    
    except Exception as e:
        error = e
    # REPORT WRITER CODE ENDS HERE

report_writer()








