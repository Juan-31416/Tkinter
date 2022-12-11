#Simple Check list app

import tkinter as tk
from tkinter import ANCHOR, BOTH, END, ttk
from tkinter.messagebox import showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Checklist")
        self.iconbitmap('check.ico')
        self.geometry('450x400')
        self.resizable(1, 0)

#define App options
my_font = ('Arial', 12)
main_color = '#6c1cbc'
button_color = '#e2cff4'

#Define functions


#Define Frames
class Frames(tk.Tk):
    #Define main frame
    def __init__(self):
        super().__init__()

        self.OpenApp

        #Define the frames
        input_frame = tk.Frame(self, bg= main_color)
        output_frame = tk.Frame(self, bg= main_color)
        button_frame = tk.Frame(self, bg= main_color)

        input_frame.pack(fill= 'x')
        output_frame.pack(fill= 'x')
        button_frame.pack(fill= 'x')

        #Input frame layout
        self.task_input = tk.Entry(input_frame, width= 35, borderwidth= 2, font= my_font)
        self.add_button = tk.Button(input_frame, text= "ADD", borderwidth= 1, bg= button_color, font= my_font, command= self.AddItem)

        self.task_input.grid(row= 0, column= 0, padx= 5, pady= 5)
        self.add_button.grid(row= 0, column= 1, padx= 5, pady= 5)

        #Output frame layout
        self.output_scrollbar = tk.Scrollbar(output_frame)
        self.output_listbox = tk.Listbox(output_frame, height= 15, width= 45, borderwidth= 2, font= my_font, yscrollcommand= self.output_scrollbar.set)
        self.output_scrollbar.config(command= self.output_listbox.yview)

        self.output_listbox.grid(row= 0, column= 0)
        self.output_scrollbar.grid(row= 0, column= 1, sticky= 'NS')


        #Buttons frame layout
        self.remove_button = tk.Button(button_frame, text= "Remove Item", borderwidth= 2, font= my_font, bg= button_color, command= self.RemoveItem)
        self.clear_button = tk.Button(button_frame, text= "Clear list", borderwidth= 2, font= my_font, bg= button_color, command= self.ClearList)
        self.save_button = tk.Button(button_frame, text= "Save list", borderwidth= 2, font= my_font, bg= button_color, command= self.SaveList)
        self.close_button = tk.Button(button_frame, text= "Close APP", borderwidth= 2, font= my_font, bg= button_color, command= self.destroy)

        self.remove_button.grid(row= 0, column= 0, padx= 10, pady= 10)
        self.clear_button.grid(row= 0, column= 1, padx= 10, pady= 10)
        self.save_button.grid(row= 0, column= 2, padx= 10, pady= 10)
        self.close_button.grid(row= 0, column= 3, padx= 10, pady= 10)


    #Define functions
    def AddItem(self):
        self.output_listbox.insert(END, self.task_input.get())
        self.task_input.delete(0, END)

    def RemoveItem(self):
       self.output_listbox.delete(ANCHOR)

    def ClearList(self):
        self.output_listbox.delete(0, END)

    def SaveList(self):
        with open("checklist.txt", 'w') as f:
            list_tuple = self.output_listbox.get(0, END)
            for item in list_tuple:
                #Take 1proper precautions to include one \n for formating purposes
                if item.endswith('\n'):
                    f.write(item)
                else:
                    f.write(item + "\n")

    def OpenApp(self):
        try:
            with open("checklist.txt", 'r') as f:
                for line in f:
                    self.output_listbox.insert(END, line)
        except:
            return 

#Initilize the App window's main loop
if __name__ == '__main__':
    app = App()
    Frames()
    app.mainloop()
