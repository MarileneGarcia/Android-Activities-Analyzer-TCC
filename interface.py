# Import Module
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
import os

# 2. The begining
def begining (root, old_frame, user_choices):
	old_frame.destroy()
	frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
	frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
	frame.grid_columnconfigure(0, weight=1)
	frame.grid_columnconfigure(1, weight=1)
	frame.grid_columnconfigure(2, weight=1)

	label = Label(frame, text ='What is the cellphone Brand', font = ("Courier", 18), background="#86acac") 
	label.grid(row = 0, column = 0, sticky = N, ipady = 10)
	choice = StringVar(frame, "none")

	button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : first_step(choice.get(), user_choices, frame))
	button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = mot, variable = choice, value = mot)
	button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = smsng, variable = choice, value = smsng)
	button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = xm, variable = choice, value = xm)
	button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = lg, variable = choice, value = lg)

	button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
	button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
	button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
	button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
	button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)



# 3. The first step, a choice of brand
def first_step(mensagem, user_choices, frame): 
	if mensagem  != "none" :
		command_dir = ""
		user_choices.append(mensagem)
		for choice in user_choices :
			command_dir = command_dir + mensagem + "/"
		messagebox.showinfo('pop-up information', 'You select: ' + mensagem)
		command = "./saida.out 1 " + command_dir
		stream = os.popen(command)
		output = stream.read()
		if "program error" in output:
			#must need to handle with the error
			messagebox.showinfo('pop-up error', str(output))
			print(str(output))
		frame.destroy()

# create root window
root = Tk()

# create global variables
user_choices = []
mot   = "Motorola"
smsng = "Samsung"
xm    = "Xiaomi"
lg    = "LG"

# root window
root.title("Android Activities Analyzer")
root.configure(background="#86acac")
root.attributes('-zoomed', True)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# 1. Adding the logo and begining
logo = PhotoImage(file="logo.png")
logo_resize = logo.subsample(2, 2)
label = tk.Label(root, image=logo_resize)
label.grid(row = 0, column = 0, rowspan = 5, sticky = W)

frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
frame.grid(row = 0, column = 1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

label = tk.Label(frame, relief = FLAT, text ='Do you want to start Android Activities Analyzer', font = ("Courier", 18), background="#86acac") 
label.grid(row = 0, column = 0, sticky = N, ipady = 10)

button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Begin', command = lambda : begining(root, frame, user_choices))
button.grid(row = 1, column = 0)





















'''Checkbutton1 = IntVar()  
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
'''
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
