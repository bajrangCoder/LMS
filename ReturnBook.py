import customtkinter
import tkinter
from database import LMS
from tkinter.messagebox import showerror, showinfo, askyesno
import datetime
import json

db = LMS("db/lms.db")

with open("config/settings.json", "r") as settings_file:
    settings = json.load(settings_file)


class ReturnBook(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.minsize(400,250)
        self.maxsize(400,250)
        self.geometry('400x250')
        self.charge_per_day = settings["charge_per_day"]
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Return Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        book_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Book ID",font=customtkinter.CTkFont(family="Verdana",size=16, weight="normal"))
        book_id_lbel.pack(pady=10)
        
        self.book_id_var = customtkinter.IntVar(self)
        self.book_id_input = customtkinter.CTkEntry(master=main_frame, width=200, textvariable=self.book_id_var)
        self.book_id_input.pack(padx=5, pady=5)
        
        return_book_btn = customtkinter.CTkButton(master=main_frame,text="Return Book",command=self.return_book)
        return_book_btn.pack(padx=10,pady=5)
    
    def return_book(self):
        book_id = self.book_id_var.get()
        
        if book_id in self.all_book_id():
            status = 'issued'
            if status in db.select_book_status(book_id):
                exp_dt = db.select_expiry_dt(book_id)
                
                std_exp_dt = datetime.datetime.strptime(exp_dt[0], "%Y-%m-%d %H:%M:%S")
                if std_exp_dt < datetime.datetime.now():
                    fine = self.total_fine(std_exp_dt)
                    conf = askyesno(title="Fine Confirmation",message=f"Student is fined, {fine[0]} for {fine[1]} days extra. Is Student paid?")
                    if conf:
                        self.return_book_func(book_id)
                    else:
                        misl_conf = askyesno(title="Miscellaneous", message="Do you want to put this book in Miscellaneous type?")
                        if misl_conf:
                            try:
                                db.update_book_status(book_id,'miscellaneous')
                                db.move_to_miscellaneous(book_id)
                                showinfo(title='Success',message='Successfully moved in miscellaneous section.')
                            except:
                                showerror(title='Server Error',message='Something went wrong. Try Again!')
                        else:
                            showerror(title="Error - fine",message="Please take the fine!")
                else:
                    self.return_book_func(book_id)
                
            else:
                showerror(title="Not Issued",message="Given book is not issued to anyone.")
        else:
            showerror(title="Not Found", message="No any book with given id.")
    
    def all_book_id(self):
        all_bookID = []
        for i in db.all_book_id():
            all_bookID.append(i[0])
        return all_bookID
    
    def return_book_func(self,book_id):
        res1 = db.return_book(book_id)
        res2 = db.update_book_status(book_id,"available")
        if res1 == "returned":
            showinfo(title="Book Returned",message=f"Book ID - {book_id}, returned to library successfully!")
        else:
            showerror(title="ERROR",message="Something went wrong! Try Again....")
    
    def total_fine(self,exp_dt):
        delta = datetime.datetime.now() - exp_dt
        total_fine = delta.days * self.charge_per_day
        return (total_fine, delta.days)
