import tkinter
import customtkinter
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from BookReport import *
from Miscellaneous import *
from PIL import ImageTk
import json

with open("config/settings.json", "r") as settings_file:
    settings = json.load(settings_file)

customtkinter.set_appearance_mode(settings["theme"])
customtkinter.set_default_color_theme(settings["color_theme"])

class Setting(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.minsize(300,450)
        self.maxsize(300,450)
        self.geometry('300x450')
        
        self.main_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        self.main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        label = customtkinter.CTkLabel(master=self.main_frame, text="Settings",font=customtkinter.CTkFont(family="Robot", size=20, weight="bold"))
        label.grid(column=1,row=0,ipady=10)
        
        theme_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Theme")
        theme_lbel.grid(column=1,row=1,padx=5, pady=5,sticky='w')
        
        self.theme_combo = customtkinter.CTkOptionMenu(self.main_frame, values=["Light", "Dark", "System"],command=self.change_theme)
        self.theme_combo.grid(column=2,row=1,padx=5, pady=5,sticky='e')
        self.theme_combo.set(settings["theme"])
        
        color_theme_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Color Theme")
        color_theme_lbel.grid(column=1,row=2,padx=5, pady=5,sticky='w')
        
        self.color_theme_combo = customtkinter.CTkOptionMenu(self.main_frame, values=["blue", "dark-blue", "green"],command=self.change_theme_color)
        self.color_theme_combo.grid(column=2,row=2,padx=5, pady=5,sticky='e')
        self.color_theme_combo.set(settings["color_theme"])
        
        issue_duration_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Issue Book Duration")
        issue_duration_lbel.grid(column=1,row=3,padx=5, pady=5,sticky='w')
        
        self.issue_duration_inp = customtkinter.CTkEntry(master=self.main_frame)
        self.issue_duration_inp.grid(column=2,row=3,padx=5,pady=5,sticky='e')
        self.issue_duration_inp.insert(0,settings["issue_duration"])
        
        charge_per_day_lbel = customtkinter.CTkLabel(master=self.main_frame,text="Charge Per Day")
        charge_per_day_lbel.grid(column=1,row=4,padx=5, pady=5,sticky='w')
        
        self.charge_per_day_inp = customtkinter.CTkEntry(master=self.main_frame)
        self.charge_per_day_inp.grid(column=2,row=4,padx=5,pady=5,sticky='e')
        self.charge_per_day_inp.insert(0,settings["charge_per_day"])
        
        footer_txt = customtkinter.CTkLabel(master=self.main_frame,text="Footer Text")
        footer_txt.grid(column=1,row=5,padx=5, pady=5,sticky='w')
        
        self.footer_txt_inp = customtkinter.CTkEntry(master=self.main_frame)
        self.footer_txt_inp.grid(column=2,row=5,padx=5,pady=5,sticky='e')
        self.footer_txt_inp.insert(0,settings["footer_txt"])
        
        self.save_setting = customtkinter.CTkButton(master=self.main_frame, text="Save",command=self.save_settings)
        self.save_setting.grid(column=2,row=6,padx=5,pady=5)
        
    def change_theme(self, new_theme_mode:str):
        settings["theme"] = new_theme_mode
        f = open("config/settings.json","w")
        json.dump(settings,f,indent=4)
        customtkinter.set_appearance_mode(new_theme_mode)
    
    def change_theme_color(self, new_theme_color:str):
        settings["color_theme"] = new_theme_color
        f = open("config/settings.json","w")
        json.dump(settings,f,indent=4)
        customtkinter.set_default_color_theme(new_theme_color)
    
    def change_issue_duration(self, issue_dur):
        settings["issue_duration"] = issue_dur
        f = open("config/settings.json","w")
        json.dump(settings,f,indent=4)
    
    def change_charge_per_day(self, per_day_charge):
        settings["charge_per_day"] = per_day_charge
        f = open("config/settings.json","w")
        json.dump(settings,f,indent=4)
    
    def change_footer_txt(self, txt):
        settings["footer_txt"] = txt
        f = open("config/settings.json","w")
        json.dump(settings,f,indent=4)
    
    def save_settings(self):
        issue_dur = self.issue_duration_inp.get()
        charge_per_day = self.charge_per_day_inp.get()
        footer_txt = self.footer_txt_inp.get()
        
        if issue_dur != None and charge_per_day != None and footer_txt != None:
            self.change_issue_duration(int(issue_dur))
            self.change_charge_per_day(int(charge_per_day))
            self.change_footer_txt(str(footer_txt))
            showinfo(title="Saved",message="Settings saved successfully! Note default color theme changes works after restart.")
        else:
            showerror(title="Empty",message="Settings shouldn't empty!")

class LMSApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.minsize(600,400)
        self.maxsize(600,400)
        self.geometry('600x400')
        icon_path = ImageTk.PhotoImage(file="logo.png")
        self.iconphoto(False, icon_path)
        
        heading_frame = customtkinter.CTkFrame(master=self,corner_radius=10)
        heading_frame.pack(padx=10,pady=10, ipadx=20, ipady=5,fill="x",anchor="n")
        
        label = customtkinter.CTkLabel(master=heading_frame, text="Library Management System",font=customtkinter.CTkFont(family="Robot", size=25, weight="bold"))
        label.pack(ipady=10)
        
        main_frame = customtkinter.CTkFrame(master=self,corner_radius=10,fg_color='transparent')
        main_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True)
        
        
        left_frame = customtkinter.CTkFrame(master=main_frame,corner_radius=10)
        left_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True,side="left")
        
        right_frame = customtkinter.CTkFrame(master=main_frame,corner_radius=10)
        right_frame.pack(padx=10,pady=10, ipadx=5, ipady=5,fill="both",expand=True,side="right")
        
        button_1 = customtkinter.CTkButton(master=left_frame,text="Add new Book",corner_radius=3, command=self.add_book_win)
        button_1.pack(padx=20, pady=10)
        
        button_2 = customtkinter.CTkButton(master=left_frame,text="Delete Book",corner_radius=3, command=self.delete_book_win)
        button_2.pack(padx=20, pady=10)
        
        button_3 = customtkinter.CTkButton(master=left_frame,text="Book List",corner_radius=3, command=self.view_book_win)
        button_3.pack(padx=20, pady=10)
        
        button_4 = customtkinter.CTkButton(master=right_frame,text="Issue Book",corner_radius=3, command=self.issue_book_win)
        button_4.pack(padx=20, pady=10)
        
        button_5 = customtkinter.CTkButton(master=right_frame,text="Return Book",corner_radius=3, command=self.return_book_win)
        button_5.pack(padx=20, pady=10)
        
        button_6 = customtkinter.CTkButton(master=right_frame,text="Book Report",corner_radius=3, command=self.book_report_win)
        button_6.pack(padx=20, pady=10)
        
        button_7 = customtkinter.CTkButton(master=right_frame,text="Miscellaneous",corner_radius=3, command=self.miscellaneous_case_win)
        button_7.pack(padx=20, pady=10)
        
        button_8 = customtkinter.CTkButton(master=left_frame,text="Setting",corner_radius=3,command=self.settings_win)
        button_8.pack(padx=20, pady=10)
        
        footer_frame = customtkinter.CTkFrame(master=self,corner_radius=8,fg_color="#f55d5d")
        footer_frame.pack(padx=20,pady=10,fill="x",anchor="s")
        dev_by_label = customtkinter.CTkLabel(master=footer_frame,text=settings["footer_txt"],bg_color="#f55d5d")
        dev_by_label.pack()
    
    def add_book_win(self):
        app = AddBook()
        app.mainloop()
    
    def delete_book_win(self):
        app = DeleteBook()
        app.mainloop()
    
    def view_book_win(self):
        app = ViewBooks()
        app.mainloop()
    
    def issue_book_win(self):
        app = IssueBook()
        app.mainloop()
    
    def return_book_win(self):
        app = ReturnBook()
        app.mainloop()
    
    def book_report_win(self):
        app = BookReport()
        app.mainloop()
    
    def miscellaneous_case_win(self):
        app = Miscellaneous()
        app.mainloop()
    
    def settings_win(self):
        app = Setting()
        app.mainloop()

if __name__ == '__main__':
    app = LMSApp()
    app.mainloop()