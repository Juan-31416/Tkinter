#Hello GUI World

import tkinter as tk
from tkinter import BOTH, Frame, StringVar, ttk, Tk, END
from turtle import bgcolor
from typing import Container
from PIL import ImageTk, Image

#Global variables
app_color = '#224870'
input_color = '#2a4494'
output_color = '#4ea5d9'

#Create root window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello GUI World!")
        self.iconbitmap("wave.ico")
        self.geometry('500x500')
        self.resizable(1,0)
        self.config(bg= app_color)

#Define functions
class SubmitName():
    def SubmitNames(self, case_style, name):
        #output_frame = OutputFrame(app)
        if case_style == 'normal':
            name_label = tk.Label(self, text= "Hello " + name + "! Keep learning Tkinter!", bg= output_color)
            
        elif case_style == 'upper':
            name_label = tk.Label(self, text= ("Hello " + name + "! Keep learning Tkinter!").upper(), bg= output_color)
        
        name_label.grid()

        #Clear the entry field for the next user
        #self.name.delete(0, END)

        return name_label



#Define Frames and labels
class InputFrame(tk.LabelFrame):
    def __init__(self, container):
        super().__init__(container, height= 100, width=400, pady= 10, bg= input_color)

        #adding position to the frame and show it
        self.pack(padx= 10)

        #Define the Entry
        self.name = tk.Entry(self, text= "Enter your name:", width= 20)
        self.name.grid(row= 0, column= 0, padx= 10, pady= 10)

        #Define the buttons & radio buttons
        self.case_style = StringVar()
        self.case_style.set('normal')
        #self.submit_name = SubmitName.SubmitNames(self.case_style.get(), self.name.get())
        self.submit_button = tk.Button(self, text= "Submit", command= SubmitName.SubmitNames(OutputFrame(app), self.case_style.get(), self.name.get()))
        self.submit_button.grid(row= 0, column= 1, padx= 5, pady= 5, ipadx=5)
        self.normal_button = tk.Radiobutton(self, text= "Normal case", variable= self.case_style, value= 'normal', bg= input_color)
        self.upper_button = tk.Radiobutton(self, text= "Upper case", variable= self.case_style, value= 'upper', bg= input_color)
        self.normal_button.grid(row= 1, column= 0, padx= 5, pady= 5)
        self.upper_button.grid(row= 1, column= 1, padx= 5, pady= 5)
        
    
        
class OutputFrame(tk.LabelFrame):
    def __init__(self, container):
        super().__init__(container, height= 400, width= 400, bg= output_color)
        
        #Add the image
        self.smile_png = ImageTk.PhotoImage(Image.open('smile.png'))
        self.smile_label = tk.Label(self, image= self.smile_png, bg= output_color)
        self.smile_label.grid()

        #adding position to the frame
        self.pack(padx= 10, pady=(0, 10), fill= BOTH, expand= True)

#Run the root window's main loop
if __name__ == "__main__":
    app = App()
    InputFrame(app)
    #OutputFrame(app)
    app.mainloop()