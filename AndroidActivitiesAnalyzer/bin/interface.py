# Import Module
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from shutil import copy
import os
import time
import traceback

# 1. Building First Screen and Root
root = Tk()
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

button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Begin', command = lambda : second_screen(root, frame, user_choices))
button.grid(row = 1, column = 0)

# 2. Building Second Screen
def second_screen (root, old_frame, user_choices):
    command = "./saida.out 0"
    stream = os.popen(command)
    output = stream.read()
    if "program error" in output:
        #must need to handle with the error, finish the program
        messagebox.showerror('pop-up error', str(output))
        print(str(output))

    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='What is the cellphone Brand', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    choice = StringVar(frame, "")

    button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : first_step_algorithm(choice.get(), user_choices, frame))
    button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = mot, variable = choice, value = mot)
    button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = smsng, variable = choice, value = smsng)
    button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = xm, variable = choice, value = xm)
    button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = lg, variable = choice, value = lg)

    button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
    button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)


# 3. The choice of brand
def first_step_algorithm (mensagem, user_choices, frame):
    if verification(mensagem, user_choices) :
        third_screen(root, frame, user_choices)


# 4. Building Third Screen
def third_screen (root, old_frame, user_choices):
    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='What is the cellphone Model', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)

    warning = Label(frame, text ='Please, do not use space, or any special caracteres', font = ("Courier", 10), background="#86acac") 
    warning.grid(row = 1, column = 0, sticky = N)

    choice = StringVar(frame, "")
    entry = tk.Entry(frame, textvariable = choice, font=('calibre',10,'normal'))
    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : second_step_algorithm(choice.get(), user_choices, frame))
    button.grid(row = 3, column = 0, sticky = N, pady = 2, padx = 10)
    entry.grid(row = 2, column = 0, sticky = N, pady = 2, padx = 10, ipady = 5)  
    
# 5. The choice of model
def second_step_algorithm (mensagem, user_choices, frame): 
    if verification(mensagem, user_choices) :
        fourth_screen(root, frame, user_choices)

# 6. Building Fourth Screen
def fourth_screen (root, old_frame, user_choices):
    old_frame.destroy()
    cam   = "Camera"
    modem = "Modem"
    wsl   = "Network"
    bt    = "Battery"

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='What is the System', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    choice = StringVar(frame, "")

    button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : third_step_algorithm(choice.get(), user_choices, frame))
    button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = cam, variable = choice, value = cam)
    button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = modem, variable = choice, value = modem)
    button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = wsl, variable = choice, value = wsl)
    button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = bt, variable = choice, value = bt)

    button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
    button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)

#7. The choice of system
def third_step_algorithm (mensagem, user_choices, frame): 
    if verification(mensagem, user_choices) :
        fifth_screen(root, frame, user_choices)

# 8. Building Fifth Screen
def fifth_screen (root, old_frame, user_choices):
    old_frame.destroy()
    ev   = "Event"
    sys = "System"
    main   = "Main"
    rd    = "Radio"

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='What is the Buffer', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    choice = StringVar(frame, "")

    button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : fouth_step_algorithm(choice.get(), user_choices, frame))
    button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = ev, variable = choice, value = ev)
    button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = sys, variable = choice, value = sys)
    button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = main, variable = choice, value = main)
    button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = rd, variable = choice, value = rd)

    button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
    button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)

#7. The choice of system
def fouth_step_algorithm (mensagem, user_choices, frame): 
    if verification(mensagem, user_choices) :
        sixth_screen(root, frame, user_choices)

# 8. Building Fifth Screen
def sixth_screen (root, old_frame, user_choices):
    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='Attach a Log file', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    log_file = StringVar(frame, "")

    warning = Label(frame, text ='text file is the format required*', font = ("Courier", 10), background="#86acac") 
    warning.grid(row = 1, column = 0, sticky = NE)

    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Choose File', command = lambda : open_file(root, frame))
    button.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10)

# 8. Finish Screen
def finish_program (root, old_frame):
    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Finish program', command = lambda : finish(root, frame))
    button.grid(row = 1, column = 0, sticky = N, pady = 2, padx = 10)


# Common Functions
def verification (mensagem, user_choices): 
    msg = "".join(c for c in mensagem if c.isalnum())
    if msg  != "" :
        command_dir = ""
        user_choices.append(msg)
        for choice in user_choices :
            command_dir = command_dir + choice + "/"
        if messagebox.askyesno('pop-up information', 'You select: ' + msg) :
            command = "./saida.out 1 " + command_dir
            stream = os.popen(command)
            output = stream.read()

            if "program error" in output:
                #must need to handle with the error, finish the program
                messagebox.showerror('pop-up error', str(output))
                print(str(output))
                #return False
                #return True
        return True
    else:
        return False

def open_file(root, frame):
    file_path = filedialog.askopenfile(mode='r', filetypes=[('Text files', '*txt')])
    if file_path is not None:
        try:
            copy(file_path.name, "../config/logs.txt")
            label_log = Label(frame, text = file_path.name, font = ("Courier", 10), background="#86acac") 
            label_log.grid(row = 5, column = 0, pady = 3, sticky = NE)
            pb = Progressbar(frame, orient=HORIZONTAL, length=300, mode='determinate')
            pb.grid(row = 4, column = 0, pady=20)
            for i in range(4):
                frame.update_idletasks()
                pb['value'] += 20
                time.sleep(0.5)
            command = "./saida.out 2"
            stream = os.popen(command)
            output = stream.read()
            if "program error" in output:
                #must need to handle with the error, finish the program
                messagebox.showerror('pop-up error', str(output))
                print(str(output))
            else:
                frame.update_idletasks()
                pb['value'] += 20
                time.sleep(1)
                pb.destroy()
                label = Label(frame, text='File Uploaded Successfully!', font = ("Courier", 10), background="#86acac")
                label.grid(row = 4, column = 0, pady=10)
                finish_program(root, frame)
        except Exception: 
                traceback.print_exc()
                #must need to handle with the error, finish the program
                print(str(output))
                messagebox.showerror('pop-up error', "program error: Can not create a path: ../config/logs.txt\nprogram exit" )


def finish(root, frame):
    root.destroy()
    '''command = "./saida.out 0"
    stream = os.popen(command)
    output = stream.read()
    if "program error" in output:
        #must need to handle with the error, finish the program
        messagebox.showerror('pop-up error', str(output))
        print(str(output))'''

# Execute Tkinter
root.mainloop()
