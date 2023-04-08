import customtkinter
import tkinter
from database import LMS
from tkinter.messagebox import showerror, showwarning, showinfo
from tkcalendar import DateEntry
import datetime
import os
import sys

db = LMS(os.path.join(os.path.dirname(sys.executable), "lms.db"))

class AddBook(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(500,400)
        self.maxsize(500,400)
        self.geometry('500x400')
        dt = datetime.datetime.now()
        dt_year = dt.year
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Add New Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
        book_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Book ID",)
        book_id_lbel.grid(column=1,row=0,padx=5, pady=5)
        
        self.book_id_input = customtkinter.CTkEntry(master=main_frame,width=200)
        self.book_id_input.grid(column=2,row=0,padx=5, pady=5)
        
        book_nme_lbel = customtkinter.CTkLabel(master=main_frame,text="Book Name",)
        book_nme_lbel.grid(column=1,row=1,padx=5, pady=5)
        
        self.book_nme_input = customtkinter.CTkEntry(master=main_frame,width=200)
        self.book_nme_input.grid(column=2,row=1,padx=5, pady=5)
        
        book_author_lbel = customtkinter.CTkLabel(master=main_frame,text="Book Author",)
        book_author_lbel.grid(column=1,row=2,padx=5, pady=5)
        
        self.book_author_input = customtkinter.CTkEntry(master=main_frame,width=200)
        self.book_author_input.grid(column=2,row=2,padx=5, pady=5)
        
        book_edition_lbel = customtkinter.CTkLabel(master=main_frame,text="Book Edition",)
        book_edition_lbel.grid(column=1,row=3,padx=5, pady=5)
        
        self.book_edition_input = customtkinter.CTkEntry(master=main_frame,width=200)
        self.book_edition_input.grid(column=2,row=3,padx=5, pady=5)
        
        book_price_lbel = customtkinter.CTkLabel(master=main_frame,text="Book Price",)
        book_price_lbel.grid(column=1,row=4,padx=5, pady=5)
        
        self.book_price_input = customtkinter.CTkEntry(master=main_frame,width=200)
        self.book_price_input.grid(column=2,row=4,padx=5, pady=5)
        
        purchase_dt_lbel = customtkinter.CTkLabel(master=main_frame,text="Purchased Date",)
        purchase_dt_lbel.grid(column=1,row=5,padx=5, pady=5)
        
        self.purch_dt_var = customtkinter.StringVar(self)
        self.purchase_dt = DateEntry(main_frame, width=10,borderwidth=2, year=dt_year, textvariable=self.purch_dt_var)
        self.purchase_dt.grid(column=2,row=5,padx=5, pady=5)
        
        add_new_book_btn = customtkinter.CTkButton(master=main_frame,text="Add Book", font=customtkinter.CTkFont(family="Verdana",size=16, weight="bold"),command=self.save_new_book)
        add_new_book_btn.grid(column=2,row=6,padx=10,pady=5,ipadx=10,ipady=10)
    
    def save_new_book(self):
        book_id = self.book_id_input.get()
        book_nme = self.book_nme_input.get()
        book_author = self.book_author_input.get()
        book_edition = self.book_edition_input.get()
        book_price = self.book_price_input.get()
        purchase_dt = self.purch_dt_var.get()
        if book_id != "" and book_nme != "" and book_author != "" and book_edition != "" and book_price != "" and purchase_dt != "":
            data = (
                book_id,
                book_nme,
                book_author,
                book_edition,
                book_price,
                purchase_dt,
                "available"
            )
            
            res = db.add_new_book(data)
            if res != None or res != '':
                self.book_id_input.delete(0,'end')
                self.book_nme_input.delete(0,'end')
                self.book_author_input.delete(0,'end')
                self.book_edition_input.delete(0,'end')
                self.book_price_input.delete(0,'end')
                #self.purchase_dt_inp.delete(0,'end')
                showinfo(title="Saved",message="New book saved successfully.")
            else:
                showerror(title="Not Saved",message="Something went wrong. Please try again...")
        else:
            showerror(title="Empty Fields",message="Please fill all the details then submit!")
