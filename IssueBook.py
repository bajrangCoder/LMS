import customtkinter
import tkinter
from database import LMS
from tkinter.messagebox import showerror, showinfo
from tkinter import ttk
import datetime
import json
import os
import sys

db = LMS(os.path.join(os.path.dirname(sys.executable), "lms.db"))

settings_file_path = os.path.join(os.path.dirname(sys.executable), 'settings.json')
with open(settings_file_path, "r") as settings_file:
    settings = json.load(settings_file)

class IssueBook(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(400,250)
        self.maxsize(400,250)
        self.geometry('300x250')
        self.no_expiry_days = settings["issue_duration"]
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        self.label = customtkinter.CTkLabel(master=heading_frame, text="Issue Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        self.label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
        book_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Book ID")
        book_id_lbel.grid(column=1,row=0,padx=5, pady=5)
        
        self.book_id_var = customtkinter.StringVar(self)
        self.book_id_input = customtkinter.CTkEntry(master=main_frame, width=200,textvariable=self.book_id_var)
        self.book_id_input.grid(column=2,row=0,padx=5, pady=10)
        
        student_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Student ID")
        student_id_lbel.grid(column=1,row=1,padx=5, pady=5)
        self.student_id_var = customtkinter.StringVar(self)
        self.student_id_input = customtkinter.CTkEntry(master=main_frame, width=200, textvariable=self.student_id_var)
        self.student_id_input.grid(column=2,row=1,padx=5, pady=5)
        
        issue_book_btn = customtkinter.CTkButton(master=main_frame,text="Issue Book",command=self.issue_book)
        issue_book_btn.grid(column=2,row=2,padx=10,pady=5)
    
    def issue_book(self):
        book_id = self.book_id_var.get()
        book_id = int(book_id)
        student_id = self.student_id_var.get()
        student_id = int(student_id)
        
        if book_id in self.all_book_id() and student_id in self.all_student_id():
            status = 'available'
            if status in db.select_book_status(book_id):
                cur_dt = datetime.datetime.now()
                std_cur_dt = cur_dt.isoformat(' ', 'seconds')
                data = (
                    book_id,
                    student_id,
                    std_cur_dt,
                    self.expiry_datetime()
                    )
                
                res1 = db.issue_book(data)
                res2 = db.update_book_status(book_id,"issued")
                
                if res1 != None:
                    showinfo(title="Issued",message=f"Book issued successfully to {student_id}")
                else:
                    showerror(title="Error",message="Something went wrong! Try Again..")
            else:
                showerror(title="Not Available",message="This book is not available or it is issued to another one.")
        else:
            showerror(title="Not Found",message="Book not found! or Student Not found! Please Check Book ID or Student ID and try again...")
        
    def all_book_id(self):
        all_bookID = []
        for i in db.all_book_id():
            all_bookID.append(i[0])
        return all_bookID
    
    def all_student_id(self):
        all_studentID = []
        for i in db.all_student_id():
            all_studentID.append(i[0])
        return all_studentID
    
    def expiry_datetime(self):
        exp_datetime = datetime.datetime.now()
        exp_datetime += datetime.timedelta(days=self.no_expiry_days)
        std_exp_dt = exp_datetime.isoformat(' ', 'seconds')
        return std_exp_dt
