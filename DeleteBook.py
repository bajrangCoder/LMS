import customtkinter
import tkinter
from database import LMS
from tkinter.messagebox import showerror, showinfo

db = LMS("db/lms.db")

class DeleteBook(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.minsize(400,250)
        self.maxsize(400,250)
        self.geometry('400x250')
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Delete Book",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        book_id_lbel = customtkinter.CTkLabel(master=main_frame,text="Book ID", font=customtkinter.CTkFont(family="Verdana",size=18))
        book_id_lbel.pack()
        
        self.book_id_input = customtkinter.CTkEntry(master=main_frame, width=200)
        self.book_id_input.pack(padx=5, pady=10)
        
        delete_book_btn = customtkinter.CTkButton(master=main_frame,text="Delete Book",command=self.delete_book)
        delete_book_btn.pack(padx=10,pady=10)
    
    def delete_book(self):
        res = db.delete_book(self.book_id_input.get())
        if res == 'deleted':
            showinfo(title="Deleted",message=f"Book ID : {self.book_id_input.get()}, deleted successfully.")
            self.book_id_input.delete(0,'end')
        else:
            showerror(title="Error",message=f"Book ID : {self.book_id_input.get()}, not deleted. Try Again!")
        