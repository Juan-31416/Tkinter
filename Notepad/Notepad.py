#Notepad

import tkinter as tk
from tkinter import BOTH, ttk
from tkinter.messagebox import showerror
from PIL import ImageTk, Image

bg_color = '#6c809a'
text_color = '#fffacd'
menu_color = '#dbd9db'

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Notepad")
        self.iconbitmap('pad.ico')
        self.geometry('500x500')
        self.resizable(1, 1)
        self.config(bg= bg_color)


class Layouts(tk.Frame):
    def __init__(self):
        #super().__init__(container)

        #Define the frames
        menu_frame = tk.Frame(self, bg= menu_color)
        text_frame = tk.Frame(self, bg= text_color)

        menu_frame.pack(fill= 'x')
        text_frame.pack(fill= 'x')

        #Define the buttons and controls of the menu
        #self.new_icon = ImageTk.PhotoImage(Image.open('new.png'))
        self.new_icon = Image.open('new.png')
        self.new_button = tk.Button(menu_frame, text= "image")
        self.new_button.pack()
        '''
        self.new_button = tk.Button(menu_frame, image= self.new_icon, command= self.New)
        open_icon = ImageTk.PhotoImage(Image.open('open.png'))
        self.open_button = tk.Button(menu_frame, image= open_icon, command= self.Open)
        save_icon = ImageTk.PhotoImage(Image.open('save.png'))
        self.save_button = tk.Button(menu_frame, image= save_icon, command= self.Save)
        close_icon = ImageTk.PhotoImage(Image.open('close.png'))
        self.close_button = tk.Button(menu_frame, image= close_icon, command= self.destroy)

        self.new_button.grid(row= 0, column= 0, padx= 5, pady= 10)
        self.open_button.grid(row= 0, column= 1, padx= 5, pady= 10)
        self.save_button.grid(row= 0, column= 2, padx= 5, pady= 10)
        self.close_button.grid(row= 0, column= 3, padx= 5, pady= 10)'''

        #Define the fonts, sizes and options


    def New(self):
        return 0

    def Open(self):
        return 0

    def Save(self):
        return 0


#Initialize the App window's main loop
if __name__ == '__main__':
    app = App()
    Layouts()
    app.mainloop()
