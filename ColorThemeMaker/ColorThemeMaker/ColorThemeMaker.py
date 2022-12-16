#Color Theme Maker

import tkinter as tk
from tkinter import Variable, ttk
from tkinter import filedialog

bg_color = '#FFFFFF'
button_color = '#FFFFFF'
frame_color = '#FFFFFF'
slider_color = '#FFFFFF'
my_font = 'Arial'

class App(tk.Tk):
    def set_colors(self, r, g, b):
        self.red_slider.get(r)
        self.green_slider.get(g)
        self.blue_slider.get(b)
        
    def __init__(self):
        super().__init__()

        #Window characteristics
        self.title("Color Theme Maker")
        self.iconbitmap('color_wheel.ico')
        self.geometry('600x600')
        self.resizable(0, 0)
        self.config(background= bg_color)

        #Create the frames
        top_frame = tk.Frame(bg= bg_color)
        bottom_frame = tk.Frame(bg= bg_color)

        top_frame.pack()
        bottom_frame.pack()

        #Define the elements of the top frame
        #Define the sliders and slider labels
        current_value = tk.DoubleVar()
        self.r_label = tk.Label(top_frame, text= "R", font= my_font, bg= bg_color)
        self.red_slider = ttk.Scale(top_frame, from_= 0, to= 255, orient= 'vertical', Variable= current_value ,command= Functions.HexRed(self, current_value))
        self.g_label = tk.Label(top_frame, text= "G", font= my_font, bg= bg_color)
        self.green_slider = ttk.Scale(top_frame, from_= 0, to= 255, orient= 'vertical', command= Functions.HexGreen(self, Variable))
        self.b_label = tk.Label(top_frame, text= "B", font= my_font, bg= bg_color)
        self.blue_slider = ttk.Scale(top_frame, from_= 0, to= 255, orient= 'vertical', command= Functions.HexBlue(self, Variable))

        self.r_label.grid(row= 0, column= 0, padx= 5, pady= 5, sticky= 'N')
        self.red_slider.grid(row= 0, column= 1, padx= 5, pady= 5)
        self.g_label.grid(row= 0, column= 2, padx= 5, pady= 5, sticky= 'N')
        self.green_slider.grid(row= 0, column= 3, padx= 5, pady= 5)
        self.b_label.grid(row= 0, column= 4, padx= 5, pady= 5, sticky= 'N')
        self.blue_slider.grid(row= 0, column= 5, padx= 5, pady= 5)

        #Create the fixed color buttons
        self.red_button = tk.Button(top_frame, text= "RED", font= my_font, bg= button_color, command= lambda: self.set_colors(255,0,0))
        self.green_button = tk.Button(top_frame, text= "GREEN", font= my_font, bg= button_color, command= lambda: self.set_colors(0,255,0))
        self.blue_button = tk.Button(top_frame, text= "BLUE", font= my_font, bg= button_color, command= lambda: self.set_colors(0,0,255))
        self.yellow_button = tk.Button(top_frame, text= "YELLOW", font= my_font, bg= button_color, command= lambda: self.set_colors(255,255,0))
        self.cyan_button = tk.Button(top_frame, text= "CYAN", font= my_font, bg= button_color, command= lambda: self.set_colors(0,255,255))
        self.magenta_button = tk.Button(top_frame, text= "MAGENTA", font= my_font, bg= button_color, command= lambda: self.set_colors(255,0,255))

        self.red_button.grid(row= 1, column= 0, padx= 5, pady= 5, columnspan=2, sticky= 'WE')
        self.green_button.grid(row= 1, column= 2, padx= 5, pady= 5, columnspan=2, sticky= 'WE')
        self.blue_button.grid(row= 1, column= 4, padx= 5, pady= 5, columnspan=2, sticky= 'WE')
        self.yellow_button.grid(row= 2, column= 0, padx= 5, pady= 5, columnspan=2, sticky= 'WE')
        self.cyan_button.grid(row= 2, column= 2, padx= 5, pady= 5, columnspan=2, sticky= 'WE')
        self.magenta_button.grid(row= 2, column= 4, padx= 5, pady= 5, columnspan=2, sticky= 'WE')

        #Create the control buttons
        self.store_button = tk.Button(top_frame, text= "STORE COLOR", font= my_font, bg= button_color, command= Functions.StoreColor())
        self.save_button = tk.Button(top_frame, text= "SAVE", font= my_font, bg= button_color, command= Functions.SaveColors())
        self.close_button = tk.Button(top_frame, text= "CLOSE", font= my_font, bg= button_color, command= lambda: self.quit())

        self.store_button.grid(row= 3, column= 0, padx= 5, pady= 5, columnspan= 6, sticky= 'WE')
        self.save_button.grid(row= 3, column= 6, padx= 5, pady= 5, sticky= 'WE')
        self.close_button.grid(row= 3, column= 7, padx= 5, pady= 5, sticky= 'WE')

        #Create the canvas to show the color
        self.show_color = tk.Canvas(top_frame, width= 100, height= 100, borderwidth= 5)
        self.rgb_label = tk.Label(top_frame, text= "255, 255, 255", bg= frame_color)
        self.hex_label = tk.Label(top_frame, text= "#FFFFFF", bg= frame_color)

        self.show_color.grid(row= 0, column= 6, columnspan= 2, padx= 15, pady= 10)
        self.rgb_label.grid(row= 1, column= 6, columnspan= 2, padx= 15, pady= 10)
        self.hex_label.grid(row= 2, column= 6, columnspan= 2, padx= 15, pady= 10)

        self.show_color.create_rectangle((0, 0), (1000, 1000), fill='green')#self.set_colors)

        #Define the elements of the bottom frame
        #Define the lines
        for i in range(6):
            self.radio_button_1 = tk.Radiobutton(bottom_frame, bg= button_color)
            self.restore_button_1 = tk.Button(bottom_frame, text= "Restore color", bg= button_color)
            self.rgb_label_1 = tk.Label(bottom_frame, text= "(255, 255, 255)", font= my_font, bg= bg_color)
            self.hex_label_1 = tk.Label(bottom_frame, text= "#FFFFFF", font= my_font, bg= bg_color)
            self.show_color_1 = tk.Canvas(bottom_frame, width= 50, height= 50, borderwidth= 1)

            self.radio_button_1.grid(row= i, column= 0, padx= 5, pady= 5)
            self.restore_button_1.grid(row= i, column= 1, padx= 5, pady= 5)
            self.rgb_label_1.grid(row= i, column= 2, padx= 5, pady= 5)
            self.hex_label_1.grid(row= i, column= 3, padx= 5, pady= 5)
            self.show_color_1.grid(row= i, column= 4, padx= 5, pady= 5)

#Define functions
class Functions():
    def HexRed(self, r):
        global red_value
        
        #Turn the slider value into a hex code
        red_value = hex(int(r))
        red_value = red_value.lstrip("0x")

        #If hex value is single digit lead with a 0 (0x)
        while len(red_value) < 2:
            red_value = "0" + str(red_value)

        self.UpdateColor

    def HexGreen(self, g):
        global green_value
        
        #Turn the slider value into a hex code
        green_value = hex(int(g))
        green_value = green_value.lstrip("0x")

        #If hex value is single digit lead with a 0 (0x)
        while len(green_value) < 2:
            green_value = "0" + str(green_value)

        self.UpdateColor

    def HexBlue(self, b):
        global blue_value
        
        #Turn the slider value into a hex code
        blue_value = hex(int(b))
        blue_value = blue_value.lstrip("0x")

        #If hex value is single digit lead with a 0 (0x)
        while len(blue_value) < 2:
            blue_value = "0" + str(blue_value)

        self.UpdateColor

    def UpdateColor(self):
        #Update the color box
        #self.show_color = tk.Canvas(self, bg= "#" + red_value + green_value + blue_value, height= 100, width= 100, borderwidth= 5)
        #self.show_color.create_rectangle((0, 0), (1000, 1000), fill='green')#self.set_colors)
        return 0


    def StoreColor(r, g, b):
        #Store the actual color tuple value and display the color
        global stored_colors
        
        #Get the value of each color slider and append 0's to keep formatting
        red = str(r)
        while len(red) < 3:
            red = "0" + red

        green = str(g)
        while len(green) < 3:
            green = "0" + green

        blue = str(b)
        while len(blue) < 3:
            blue = "0" + blue

        #Keep the reference of the stored color
        stored_red = r
        stored_green = g
        stored_blue = b



    def SaveColors():
        #Output the stored colors into a .txt
        file_name = filedialog.asksaveasfilename(initialdir= './', title= "Save_colors", filetypes=(('Text', '.txt'), ('All Files', '*.*')))
        
        #Open new file as write
        with open(file_name, 'w') as f:
            f.write("Color Theme Maker Output \n")
            for saved_entry in stored_colors.values():
                f.write(saved_entry[0] + "\n" + saved_entry[1] + "\n\n")



if __name__ == '__main__':
    app = App()
    app.mainloop()
