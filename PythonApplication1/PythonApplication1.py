from logging import root
from pydoc import text
import tkinter
from tkinter.ttk import tclobjs_to_py
from tkinter import BOTH, END
from tkinter import IntVar #For Radio buttons
from PIL import ImageTk, Image


################
### Basics 0 ###
################

'''
#Define a Window
root = tkinter.Tk()
root.title("Window basics!")
root.iconbitmap('thinking.ico') #iconarchive.com
root.geometry('250x700')#Widthxheight
root.resizable(1,1)#x,y resize. 0 = not able, 1 = able
root.config(bg = 'green')

#Second winddow
top = tkinter.Toplevel()
top.title("Window basics!")
top.config(bg = '#123456') #hex code
top.geometry('200x200+500+50')

#Run root window's main loop
root.mainloop()
'''

################
### Basics 1 ###
################
'''
#Labels and the Pack System
root = tkinter.Tk()
root.title("Label Basics!")
root.iconbitmap("thinking.ico")
root.geometry('400x400')
root.resizable(0,0)
root.config(bg = 'blue')

#Create widgets
name_label_1 = tkinter.Label(root, text = "Hello, my name is JPy")
name_label_1.pack()

name_label_2 = tkinter.Label(root, text = "Hello, my name is Carlos.", font = ('Arial', 18, 'bold'))
name_label_2.pack()

name_label_3 = tkinter.Label(root)
name_label_3.config(text = 'Hello, my name is Laura.')
name_label_3.config(font = ('Cambria', 10))
name_label_3.config(bg = '#ff0000')
name_label_3.pack(padx = 10, pady = 50)

name_label_4 = tkinter.Label(root, text = 'Hello, my name is Ross', bg = '#000000', fg = 'green')
name_label_4.pack(pady = (0, 10), ipadx = 50, ipady = 10, anchor = 'w')

name_label_5 = tkinter.Label(root, text = "Hello, my name is Fran", bg = '#ffffff', fg = '#123123')
name_label_5.pack(fill = BOTH, expand = True, padx = 10, pady = 10)

#Run the root window's main loop
root.mainloop()
'''

################
### Basics 2 ###
################

#Buttons and the Grid System
'''
root = tkinter.Tk()
root.title("Buttons Basics!")
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)

#Define layout
name_button = tkinter.Button(root, text= "Name")
name_button.grid(row = 0, column = 0)

time_button = tkinter.Button(root, text= 'Time', bg= '#00ffff')
time_button.grid(row= 0, column= 1)

place_button = tkinter.Button(root, text= 'Place', bg= '#00ffff', activebackground= '#ff0000')
place_button.grid(row= 0, column= 2, padx= 10, pady= 10, ipadx= 15)

day_button = tkinter.Button(root, text= "Day", bg= 'black', fg= 'white', borderwidth= 5)
day_button.grid(row= 1, column= 0, columnspan= 3, sticky= 'WE')

test_1 = tkinter.Button(root, text= "text")
test_1.grid(row= 2, column= 0, padx= 5, pady= 5)
test_2 = tkinter.Button(root, text= "text")
test_2.grid(row= 2, column= 1, padx= 5, pady= 5)
test_3= tkinter.Button(root, text= "text")
test_3.grid(row= 2, column= 2, padx= 5, pady= 5, sticky= 'W')
test_4 = tkinter.Button(root, text= "text")
test_4.grid(row= 3, column= 0, padx= 5, pady= 5)
test_5 = tkinter.Button(root, text= "text")
test_5.grid(row= 3, column= 1, padx= 5, pady= 5)
test_6 = tkinter.Button(root, text= "text")
test_6.grid(row= 3, column= 2, padx= 5, pady= 5, sticky= 'W')

#Run the root window's main loop
root.mainloop()
'''

################
### Basics 3 ###
################

#Frames
'''
root = tkinter.Tk()
root.title("Frames Basics!")
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)

#Not using frames
#name_label = tkinter.Label(root, text= "Enter your name")
#name_label.pack()
#name_button = tkinter.Button(root, text= "Submit your name")
#name_button.grid(row= 0, column= 0)

#using frames
#Define frames
pack_frame = tkinter.Frame(root, bg= 'red')
grid_frame_1 = tkinter.Frame(root, bg= 'blue')
grid_frame_2 = tkinter.Frame(root, borderwidth=5)#text= "Grid system rules!", 

#Pack frames onto root
pack_frame.pack(fill= BOTH, expand= True)
grid_frame_1.pack(fill= 'x', expand= True)
grid_frame_2.pack(fill= BOTH, expand= True, padx= 10, pady= 10)

#pack frame
tkinter.Label(pack_frame, text= "text").pack()
tkinter.Label(pack_frame, text= "text").pack()
tkinter.Label(pack_frame, text= "text").pack()

#Grid 1 layout
tkinter.Label(grid_frame_1, text= "text").grid(row=0, column=0)
tkinter.Label(grid_frame_1, text= "text").grid(row=1, column=1)
tkinter.Label(grid_frame_1, text= "text").grid(row=2, column=2)
#tkinter.Label(grid_frame_1, text= "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row= 3, column=0)

#Grid 2 layout
tkinter.Label(grid_frame_2, text= "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row= 0, column=0)


#Run the window's mail loop
root.mainloop()
'''

################
### Basics 4 ###
################

#Entries, Functions, and Lambdas
root = tkinter.Tk()
root.title("Entry Basics!")
root.iconbitmap('thinking.ico')
root.geometry('500x500')
root.resizable(0,0)

#Define Functions
def make_label():
    #Print a label to the app
    text = tkinter.Label(output_frame, text= text_entry.get(), bg= '#ff0000', fg= '#ffffff')
    text.pack()

    text_entry.delete(0, END)

def count_up(number):
    #Count on the app
    global value #Make the changes in this variable global

    text = tkinter.Label(output_frame, text= number, bg= '#ff0000', fg= '#ffffff')
    text.pack()

    value = value + 1

#Define frames
input_frame = tkinter.Frame(root, bg= '#0000ff', width= 500, height= 100)
output_frame = tkinter.Frame(root, bg= '#ff0000', width=500, height= 400)
input_frame.pack(padx= 10, pady= 0)
output_frame.pack(padx= 10, pady= 10)

#Add inputs
text_entry = tkinter.Entry(input_frame, width= 40)
text_entry.grid(row= 0, column= 0, padx= 5, pady= 5)
input_frame.grid_propagate(0) #Frame will not resize to the widget that it contains

print_button = tkinter.Button(input_frame, text= "Print!", command= make_label)
print_button.grid(row= 0, column= 1, padx= 5, pady= 5, ipadx= 30)

#Keep output frame size
output_frame.pack_propagate(0)

#Pass a parameter with lambda
value = 0
count_button = tkinter.Button(input_frame, text= "Count", command= lambda:count_up(value))
count_button.grid(row= 1, column=0, columnspan=2, padx= 5, pady= 5, sticky='WE')

#Run the window's main loop
root.mainloop()



################
### Basics 5 ###
################

#Radio Buttons
'''
root = tkinter.Tk()
root.title("Radio Button Basics!")
root.iconbitmap("thinking.ico")
root.geometry('350x350')
root.resizable(0,0)

#Define functions
def make_label():
    #Print to the screen
    if number.get() == 1:
        num_label = tkinter.Label(output_frame, text= "1 one 1")
    elif number.get() == 2:
        num_label = tkinter.Label(output_frame, text= "2 two 2")

    num_label.pack()

#Define Frames
input_frame = tkinter.LabelFrame(root, text= "This is fun!", width= 350, height= 100)
output_frame = tkinter.Frame(root, width= 350, height= 250)
input_frame.pack(padx= 10, pady= 10)
output_frame.pack(padx= 10, pady= 10)

#Define Widgets & Radio buttons
number = IntVar()
number.set(1)
radio_1 = tkinter.Radiobutton(input_frame, text= "Print the number one!", variable= number, value= 1)
radio_2 = tkinter.Radiobutton(input_frame, text= "Print the number two!", variable= number, value= 2)
radio_3 = tkinter.Button(input_frame, text= "Print the number!", command= make_label)

radio_1.grid(row= 0, column= 0, padx= 10, pady= 10)
radio_2.grid(row=0, column= 1, padx= 10, pady= 10)
radio_3.grid(row= 1, column= 0, columnspan= 2, padx= 10, pady= 10)

#Runn the root window main loop
root.mainloop()
'''


################
### Basics 6 ###
################
'''
#Images
root = tkinter.Tk()
root.title("Image Basics!")
root.iconbitmap('thinking.ico')
root.geometry('700x700')

#Define functions
def make_image():
    #Using PIL for jpg
    global cat_image #Return the image out of the function

    cat_image = ImageTk.PhotoImage(Image.open('cat.jpg'))
    cat_label = tkinter.Label(root, image= cat_image)
    cat_label.pack()

#Basics works for png
#Create the image
my_image = tkinter.PhotoImage(file= 'shield.png')
#Put it into a label/button/widget
my_label = tkinter.Label(root, image= my_image)
my_label.pack()

my_button = tkinter.Button(root, image= my_image)
my_button.pack()

#Basics works for jpg
#cat_image = tkinter.PhotoImage(file= 'cat.jpg')
#cat_label = tkinter.Label(root, image= cat_image)

make_image()

#Run root window's main loop
root.mainloop()
'''