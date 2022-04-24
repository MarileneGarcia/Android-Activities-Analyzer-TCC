# Import Module
from tkinter import * 
from tkinter.ttk import *

# create root window
root = Tk()

# root window
root.title("Android Activities Analyzer")
root.configure(background="#86acac")
root.attributes('-zoomed', True)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# adding the logo
logo = PhotoImage(file="logo.png")
logo_resize = logo.subsample(2, 2)
label_1 = Label(root, image=logo_resize)
label_1.grid(row = 0, column = 0, rowspan = 6, sticky = W)

# first step
label_2 = Label(root, text ='What is the cellphone Brand', font = 24, background="#86acac") 
label_2.grid(row = 0, column = 1, sticky = N)
  
Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()

# This will create style checkbutton
style_1 = Style()
style_1.configure('Checkbutton', background="#86acac")

Button1 = Checkbutton(root, text = "Motorola", variable = Checkbutton1, onvalue = 1, offvalue = 0)
Button2 = Checkbutton(root, text = "Samsung", variable = Checkbutton2, onvalue = 1, offvalue = 0)
Button3 = Checkbutton(root, text = "Xiaomi", variable = Checkbutton3, onvalue = 1, offvalue = 0)
Button4 = Checkbutton(root, text = "LG", variable = Checkbutton4, onvalue = 1, offvalue = 0)
    
Button1.grid(row = 1, column = 1, sticky = NW, pady = 2, padx = 10)  
Button2.grid(row = 2, column = 1, sticky = NW, pady = 2, padx = 10)
Button3.grid(row = 3, column = 1, sticky = NW, pady = 2, padx = 10)
Button4.grid(row = 4, column = 1, sticky = NW, pady = 2, padx = 10)

'''# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when
# button is clicked
def clicked():

	res = "You wrote" + txt.get()
	lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
			fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)'''

# Execute Tkinter
root.mainloop()
