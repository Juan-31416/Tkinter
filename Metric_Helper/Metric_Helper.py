#Conversion Helper

from email.errors import StartBoundaryNotFoundDefect
import tkinter as tk
from tkinter import BOTH, END, ttk
from tkinter.messagebox import showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Metric Helper')
        self.iconbitmap('ruler.ico')
        self.geometry('400x200')
        self.resizable(0, 0)

bg_color = '#c75c5c'
button_color = '#f5cf87'

class ConversionFunctions():
    @staticmethod
    def ConvertedValue(self, value, start_prefix, end_prefix):
        self.metric_values ={
            'femto': 10**-15,
            'pico': 10**-12,
            'nano': 10**-9,
            'micro': 10**-6,
            'mili': 10**-3,
            'centi': 10**-2,
            'deci': 10**-1,
            'base value': 10**0,
            'Deca': 10**1,
            'Hecto': 10**2,
            'Kilo': 10**3,
            'Mega': 10**6,
            'Giga': 10**9,
            'Tera': 10**12,
            'Peta': 10**15
            }

        #Convert to the base units
        self.base_value = value*self.metric_values[start_prefix]
        #Convert to the new metrix value
        self.end_value = self.base_value/self.metric_values[end_prefix]

        return self.end_value

class ConversionFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container, bg=bg_color)#'#B90E0A') Crimson bg

        self.pack(padx= 1, pady= 1, fill= BOTH, expand= True)

        #Define functions
        def Convert():
            try:
                v = float(self.input_value.get())
                start_prefix = self.input_units.get()
                end_prefix = self.output_units.get()

                #Clear the output field
                self.output_value.delete(0, END)

                conversion = ConversionFunctions.ConvertedValue(self, v, start_prefix, end_prefix)
                self.output_value.insert(0, str(conversion))

            except ValueError as error:
                showerror(title= "Error", message= error)

        #Define labels
        self.value = tk.StringVar()
        self.input_value = tk.Entry(self, width= 20, borderwidth= 3)
        self.equal_label = ttk.Label(self, text= "=", background= bg_color)
        self.output_value = tk.Entry(self, width= 20, borderwidth= 3)

        self.input_value.grid(row= 0, column= 0, padx= 10, pady= 10)
        self.equal_label.grid(row= 0, column=1, padx= 5, pady= 10)
        self.output_value.grid(row= 0, column= 2, padx= 10, pady= 10)

        self.input_value.insert(0, "Enter your quantity")
        
        #Create the selectors
        metric_list = ["femto", "pico", "nano", "micro", "mili", "centi", "deci", "base value", "Deca", "Hecto", "Kilo", "Mega", "Giga", "Tera", "Peta"]

        #self.input_choice = tk.StringVar()
        #self.output_choice = tk.StringVar()
        
        self.input_units = ttk.Combobox(self, value= metric_list, justify= 'center')
        #self.input_units = ttk.OptionMenu(self, self.input_choice, *metric_list)
        self.output_units = ttk.Combobox(self, value= metric_list, justify= 'center')
        #self.output_units = ttk.OptionMenu(self, self.output_choice, *metric_list)
        self.to_label = ttk.Label(self, text= "to", background= bg_color)

        self.input_units.grid(row=1, column= 0, padx= 10, pady= 10)
        self.to_label.grid(row= 1, column= 1, padx= 5, pady= 10)
        self.output_units.grid(row=1, column= 2, padx= 10, pady= 10)

        self.input_units.set("base value")
        self.output_units.set("base value")

        '''self.input_units['values'] = ['mili', 'centi', 'deci', 'base value']
        self.input_units['state'] = 'readonly' #Prevent typing a value
        self.output_units['values'] = ['mili', 'centi', 'deci', 'base value']
        self.output_units['state'] = 'readonly'
        '''

        #Create the button
        self.conversion_button = tk.Button(self, text= "Convert", bg= button_color, command= Convert)
        #self.conversion_button['command'] = self.Convert
        self.conversion_button.grid(row= 2, column= 0, padx= 10, pady= 10, columnspan= 3)
        
#Initialize the main App
if __name__ == '__main__':
    app = App()
    ConversionFrame(app)
    app.mainloop()
