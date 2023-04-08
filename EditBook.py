import customtkinter
import tkinter
from database import LMS
from tkinter.messagebox import showerror, showwarning, showinfo
from tkcalendar import DateEntry
import os
import sys

db = LMS(os.path.join(os.path.dirname(sys.executable), "lms.db"))

class EditBook(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(500,490)
        self.maxsize(500,490)
        self.geometry('500x490')
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Edit Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        first_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        first_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        book_id_lbel1 = customtkinter.CTkLabel(master=first_frame,text="Book ID",font=customtkinter.CTkFont(family="Verdana",size=16, weight="bold"))
        book_id_lbel1.grid(column=1,row=0,padx=10, pady=10)
        
        self.book_id_input1 = customtkinter.CTkEntry(master=first_frame,width=200)
        self.book_id_input1.grid(column=2,row=0,padx=5, pady=10)
        
        search_book_det_btn = customtkinter.CTkButton(master=first_frame,text="Search", font=customtkinter.CTkFont(family="Verdana",size=16, weight="bold"),command=self.search_book_detail)
        search_book_det_btn.grid(column=3,row=0,padx=5,pady=10)
        
        self.main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        self.main_frame.pack_forget()
        
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        
        book_id_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Book ID",)
        book_id_lbel.grid(column=1,row=0,padx=5, pady=5)
        
        self.id_var = customtkinter.StringVar(self)
        self.book_id_input = customtkinter.CTkEntry(master=self.main_frame,width=200, textvariable=self.id_var, state='disabled')
        self.book_id_input.grid(column=2,row=0,padx=5, pady=5)
        
        book_nme_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Book Name",)
        book_nme_lbel.grid(column=1,row=1,padx=5, pady=5)
        
        self.name_var = customtkinter.StringVar(self)
        self.book_nme_input = customtkinter.CTkEntry(master=self.main_frame,width=200, textvariable=self.name_var)
        self.book_nme_input.grid(column=2,row=1,padx=5, pady=5)
        
        book_author_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Book Author",)
        book_author_lbel.grid(column=1,row=2,padx=5, pady=5)
        
        self.author_var = customtkinter.StringVar(self)
        self.book_author_input = customtkinter.CTkEntry(master=self.main_frame,width=200, textvariable=self.author_var)
        self.book_author_input.grid(column=2,row=2,padx=5, pady=5)
        
        book_edition_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Book Edition",)
        book_edition_lbel.grid(column=1,row=3,padx=5, pady=5)
        
        self.edition_var = customtkinter.StringVar(self)
        self.book_edition_input = customtkinter.CTkEntry(master=self.main_frame,width=200, textvariable=self.edition_var)
        self.book_edition_input.grid(column=2,row=3,padx=5, pady=5)
        
        book_price_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Book Price",)
        book_price_lbel.grid(column=1,row=4,padx=5, pady=5)
        
        self.price_var = customtkinter.StringVar(self)
        self.book_price_input = customtkinter.CTkEntry(master=self.main_frame,width=200, textvariable=self.price_var)
        self.book_price_input.grid(column=2,row=4,padx=5, pady=5)
        
        purchase_dt_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Purchased Date",)
        purchase_dt_lbel.grid(column=1,row=5,padx=5, pady=5)
        
        self.purchase_dt_var = customtkinter.StringVar(self)
        self.purchase_dt = DateEntry(self.main_frame, width=10,borderwidth=2, textvariable=self.purchase_dt_var)
        self.purchase_dt.grid(column=2,row=5,padx=5, pady=5)
        
        update_new_book_btn = customtkinter.CTkButton(master=self.main_frame,text="Update", font=customtkinter.CTkFont(family="Verdana",size=16, weight="bold"),command=self.update_book)
        update_new_book_btn.grid(column=2,row=6,padx=10,pady=5,ipadx=10,ipady=10)
    
    def search_book_detail(self):
        book_id = self.book_id_input1.get()
        book_id = int(book_id)
        book_details = db.select_book_detail(book_id)
        if book_details != None:
            self.id_var.set(book_details[0])
            self.name_var.set(book_details[1])
            self.author_var.set(book_details[2])
            self.edition_var.set(book_details[3])
            self.price_var.set(book_details[4])
            self.purchase_dt_var.set(book_details[5])
            self.main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        else:
            showerror(title="Not Found", message="Book Not Found")
        
    
    def update_book(self):
        book_id = self.id_var.get()
        book_nme = self.name_var.get()
        book_author = self.author_var.get()
        book_edition = self.edition_var.get()
        book_price = self.price_var.get()
        purchase_dt = self.purchase_dt_var.get()
        if book_id != "" and book_nme != "" and book_author != "" and book_edition != "" and book_price != "" and purchase_dt != "":
            data = (
                book_id,
                book_nme,
                book_author,
                book_edition,
                book_price,
                purchase_dt,
                book_id
            )
            
            res = db.update_book_details(data)
            if res != None or res != '':
                showinfo(title="Saved",message="Book updated successfully.")
            else:
                showerror(title="Not Saved",message="Something went wrong. Please try again...")
        else:
            showerror(title="Empty Fields",message="Please fill all the details then submit!")
    
    