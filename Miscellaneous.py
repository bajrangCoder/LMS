import customtkinter
import tkinter
from tkinter import ttk
from database import LMS
from tkinter.messagebox import showinfo
import os
import sys

db = LMS(os.path.join(os.path.dirname(sys.executable), "lms.db"))


class Miscellaneous(customtkinter.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Library Management System")
        self.minsize(1300,450)
        self.maxsize(1300,450)
        self.geometry('1300x450')
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Miscellaneous Books",font=customtkinter.CTkFont(family="Robot",size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        columns = ('book_id', 'book_name', 'book_author', 'book_edition', 'book_price', 'purchase_dt', 'status')

        self.tree = ttk.Treeview(main_frame, columns=columns, show='headings')
        
        # define headings
        self.tree.heading('book_id', text='Book ID')
        self.tree.heading('book_name', text='Name')
        self.tree.heading('book_author', text='Author')
        self.tree.heading('book_edition', text='Edition')
        self.tree.heading('book_price', text='Price')
        self.tree.heading('purchase_dt', text='Purchased Date')
        self.tree.heading('status', text='Status')
        
        self.load_book_data()
        
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        
        self.tree.grid(row=0,column=0,sticky='nsew')
        
        scrollbar = customtkinter.CTkScrollbar(main_frame, orientation='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky='ns')

    def load_book_data(self):
        book_list = db.miscellaneous_books()
        for i in book_list:
            self.tree.insert('', tkinter.END, values=i)
    
    def item_selected(self,event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
        
        self.details_win(record)
    
    def details_win(self,record):
        window = customtkinter.CTkToplevel(self)
        window.title("Library Management System")
        window.minsize(430,630)
        window.maxsize(430,630)
        window.geometry('430x630')
        
        main_frame = customtkinter.CTkFrame(master=window,corner_radius=10,height=100)
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        label = customtkinter.CTkLabel(master=main_frame, text="Details",font=customtkinter.CTkFont(family="Robot", size=30, weight="bold"),fg_color="#ca1a27",corner_radius=8,width=150)
        label.grid(column=0,row=0,pady=15,padx=5,ipadx=5,ipady=5,sticky='e')
        
        lbel1 = customtkinter.CTkLabel(master=main_frame,text="Book ID :",font=customtkinter.CTkFont(family="Verdana", size=25, weight="normal"))
        lbel1.grid(column=0,row=1,padx=5, pady=5,sticky='e')
        
        tvar1 = customtkinter.IntVar(window,record[0])
        inp1 = customtkinter.CTkEntry(master=main_frame,font=customtkinter.CTkFont(family="Verdana", size=20, weight="normal"),width=220,state='disabled', textvariable=tvar1)
        inp1.grid(column=1,row=1,padx=5, pady=5,sticky='w')
        
        lbel3 = customtkinter.CTkLabel(master=main_frame,text="Book Name :",font=customtkinter.CTkFont(family="Verdana", size=25, weight="normal"))
        lbel3.grid(column=0,row=2,padx=5, pady=5,sticky='e')
        
        tvar2 = customtkinter.StringVar(window,record[1])
        lbel4 = customtkinter.CTkEntry(master=main_frame, font=customtkinter.CTkFont(family="Verdana", size=20, weight="normal"),width=220,state='disabled', textvariable=tvar2)
        lbel4.grid(column=1,row=2,padx=5, pady=5,sticky='w')
        
        lbel5 = customtkinter.CTkLabel(master=main_frame,text="Book Author :",font=customtkinter.CTkFont(family="Verdana", size=25, weight="normal"))
        lbel5.grid(column=0,row=3,padx=5, pady=5,sticky='e')
        
        tvar3 = customtkinter.StringVar(window,record[2])
        lbel6 = customtkinter.CTkEntry(master=main_frame,font=customtkinter.CTkFont(family="Verdana", size=20, weight="normal"),width=220,state='disabled', textvariable=tvar3)
        lbel6.grid(column=1,row=3,padx=5, pady=5,sticky='w')
        
        lbel7 = customtkinter.CTkLabel(master=main_frame,text="Book Edition :",font=customtkinter.CTkFont(family="Verdana", size=25, weight="normal"))
        lbel7.grid(column=0,row=4,padx=5, pady=5,sticky='e')
        
        tvar4 = customtkinter.StringVar(window,record[3])
        lbel8 = customtkinter.CTkEntry(master=main_frame,font=customtkinter.CTkFont(family="Verdana", size=20, weight="normal"),width=220,state='disabled', textvariable=tvar4)
        lbel8.grid(column=1,row=4,padx=5, pady=5,sticky='w')
        
        lbel9 = customtkinter.CTkLabel(master=main_frame,text="Book Price :",font=customtkinter.CTkFont(family="Verdana", size=25, weight="normal"))
        lbel9.grid(column=0,row=5,padx=5, pady=5,sticky='e')
        
        tvar5 = customtkinter.StringVar(window,record[4])
        lbel10 = customtkinter.CTkEntry(master=main_frame, font=customtkinter.CTkFont(family="Verdana", size=20, weight="normal"),width=220,state='disabled', textvariable=tvar5)
        lbel10.grid(column=1,row=5,padx=5, pady=5,sticky='w')
        
        lbel11 = customtkinter.CTkLabel(master=main_frame,text="Purchase Date:",font=customtkinter.CTkFont(family="Verdana", size=25, weight="normal"))
        lbel11.grid(column=0,row=6,padx=5, pady=5,sticky='e')
        
        tvar6 = customtkinter.StringVar(window,record[5])
        lbel12 = customtkinter.CTkEntry(master=main_frame, font=customtkinter.CTkFont(family="Verdana", size=20, weight="normal"),width=220,state='disabled', textvariable=tvar6)
        lbel12.grid(column=1,row=6,padx=5, pady=5,sticky='w')
        lb1 = customtkinter.CTkLabel(master=window,text="Miscellaneous Book",fg_color="#e30f67",corner_radius=8,font=customtkinter.CTkFont(family='Tahoma',size=20,weight='bold'))
        lb1.pack(ipady=5,ipadx=5,fill='x',anchor='n')
        

