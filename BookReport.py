import customtkinter
import tkinter
from database import LMS
from tkinter.messagebox import showerror, showinfo
from tkinter import filedialog
import pandas as pd
import os
import sys

db = LMS(os.path.join(os.path.dirname(sys.executable), "lms.db"))

class BookReport(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(400,300)
        self.maxsize(400,300)
        self.geometry('400x300')
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Generate Book Report",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        avlb_book_export_btn = customtkinter.CTkButton(master=main_frame,text="Export Available Book",command=self.export_available_book)
        avlb_book_export_btn.pack(padx=10,pady=10)
        
        issue_book_exp_btn = customtkinter.CTkButton(master=main_frame,text="Export Issued Book",command=self.export_issued_book)
        issue_book_exp_btn.pack(padx=10,pady=10)
        
        export_all_book_btn = customtkinter.CTkButton(master=main_frame,text="Export All Book",command=self.export_all_book)
        export_all_book_btn.pack(padx=10,pady=10)
        
        export_fine_btn = customtkinter.CTkButton(master=main_frame,text="Export Fine Details",command=self.export_fine_detail)
        export_fine_btn.pack(padx=10,pady=10)
        
    def export_available_book(self):
        dbt = db.all_available_book()
        data = pd.read_sql_query(dbt[0],dbt[1])
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/available_books.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")
    
    def export_issued_book(self):
        dbt = db.all_issued_book()
        data = pd.read_sql_query(dbt[0],dbt[1])
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/issued_books.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")
    
    def export_all_book(self):
        dbt = db.all_books()
        data = pd.read_sql_query(dbt[0],dbt[1])
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/all_books.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")
    
    def export_fine_detail(self):
        dbt = db.fine_detail()
        data = pd.read_sql_query(dbt[0],dbt[1])
        try:
            selected_folder = filedialog.askdirectory()
            data.to_excel(f"{selected_folder}/fine_details.xlsx")
            showinfo(title="Success",message="Exported successfully")
        except:
            showerror(title="Error", message="Location not selected...")