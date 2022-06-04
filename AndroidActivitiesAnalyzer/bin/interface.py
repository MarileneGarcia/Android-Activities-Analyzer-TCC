# Import Modules
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from shutil import copy
import os
import time
import traceback
from turtle import st
from igraph import *

# Building screens

# Screen 0
root = Tk()
user_choices = []

root.title("Android Activities Analyzer")
root.configure(background="#86acac")
root.attributes('-zoomed', True)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)

logo = PhotoImage(file="logo.png")
logo_resize = logo.subsample(3, 3)
label = tk.Label(root, image=logo_resize)
label.grid(row = 0, column = 0, rowspan = 5, sticky = NW)

frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
frame.grid(row = 0, column = 1, rowspan = 5, sticky = NW)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

label = tk.Label(frame, relief = FLAT, text ='Do you want to start Android Activities Analyzer', font = ("Courier", 18), background="#86acac") 
label.grid(row = 0, column = 0, sticky = N, ipady = 10)

button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Begin', command = lambda : screen_1(root, frame, user_choices))
button.grid(row = 1, column = 0)

# Screen 1
def screen_1 (root, old_frame, user_choices):
    command = "./program.out 0"
    stream = os.popen(command)
    output = stream.read()
    if "program error" in output:
        messagebox.showerror('pop-up error', str(output))
        finish_program (root, old_frame)

    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='What is the Android Version', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    choice = StringVar(frame, "")

    button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : inspect_screen_1(choice.get(), user_choices, frame))
    button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = "Android 12", variable = choice, value = "android12")
    button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = "Android 11", variable = choice, value = "android11")
    button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = "Android 10", variable = choice, value = "android10")
    button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = "Android 09", variable = choice, value = "android09")

    button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
    button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)

def inspect_screen_1 (mensagem, user_choices, frame):
    if verification(mensagem, user_choices):
        screen_2(root, frame, user_choices)

# Screen 2
def screen_2 (root, old_frame, user_choices):
    mot   = "Motorola"
    smsng = "Samsung"
    xm    = "Xiaomi"
    lg    = "LG"

    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='What is the cellphone Brand', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    choice = StringVar(frame, "")

    button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : inspect_screen_2(choice.get(), user_choices, frame))
    button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = mot, variable = choice, value = mot)
    button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = smsng, variable = choice, value = smsng)
    button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = xm, variable = choice, value = xm)
    button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = lg, variable = choice, value = lg)

    button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
    button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)

def inspect_screen_2 (mensagem, user_choices, frame):
    if verification(mensagem, user_choices):
        screen_3(root, frame, user_choices)


# Screen 3
def screen_3 (root, old_frame, user_choices):
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
    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : inspect_screen_3(choice.get(), user_choices, frame))
    button.grid(row = 3, column = 0, sticky = N, pady = 2, padx = 10)
    entry.grid(row = 2, column = 0, sticky = N, pady = 2, padx = 10, ipady = 5)  
    
def inspect_screen_3 (mensagem, user_choices, frame): 
    if verification(mensagem, user_choices):
        screen_4(root, frame, user_choices)


# Screen 4
def screen_4 (root, old_frame, user_choices):
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

    button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : inspect_screen_4(choice.get(), user_choices, frame))
    button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = cam, variable = choice, value = cam)
    button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = modem, variable = choice, value = modem)
    button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = wsl, variable = choice, value = wsl)
    button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = bt, variable = choice, value = bt)

    button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
    button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)

def inspect_screen_4 (mensagem, user_choices, frame): 
    if verification(mensagem, user_choices):
        screen_5(root, frame, user_choices)


# Screen 5
def screen_5 (root, old_frame, user_choices):
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

    button_0 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : inspect_screen_5(choice.get(), user_choices, frame))
    button_1 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = ev, variable = choice, value = ev)
    button_2 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = sys, variable = choice, value = sys)
    button_3 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = main, variable = choice, value = main)
    button_4 = tk.Radiobutton(frame, background="#86acac", font = ("Courier", 14), text = rd, variable = choice, value = rd)

    button_0.grid(row = 5, column = 0, sticky = N, pady = 2, padx = 10)
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)  
    button_2.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_3.grid(row = 3, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)
    button_4.grid(row = 4, column = 0, sticky = NW, pady = 2, padx = 10, ipady = 1)

def inspect_screen_5 (mensagem, user_choices, frame): 
    if verification(mensagem, user_choices):
        dir = verification_target(user_choices)
        if dir != None :
            screen_6(root, frame, user_choices, dir)


# Screen 6
def screen_6 (root, old_frame, user_choices, dir):
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

    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Choose File', command = lambda : open_file(root, frame, user_choices, dir))
    button.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10)

    print = user_choices

def open_file(root, frame, user_choices, dir):
    file_path = filedialog.askopenfile(mode='r', filetypes=[('Text files', '*txt')])
    if file_path is not None:
        try:
            copy(file_path.name, "../config/pids/logs.txt")
            copy(file_path.name, "../config/activities/" + dir + "target.txt")
            label_log = Label(frame, text = file_path.name, font = ("Courier", 10), background="#86acac") 
            label_log.grid(row = 5, column = 0, pady = 3, sticky = NE)
            pb = Progressbar(frame, orient=HORIZONTAL, length=300, mode='determinate')
            pb.grid(row = 4, column = 0, pady=20)
            for i in range(4):
                frame.update_idletasks()
                pb['value'] += 20
                time.sleep(0.5)
            command = "./program.out 2"
            stream = os.popen(command)
            output = stream.read()
            if "program error" in output:
                messagebox.showerror('pop-up error', str(output))
                finish_program (root, frame)
            else:
                frame.update_idletasks()
                pb['value'] += 20
                time.sleep(1)
                pb.destroy()
                label = Label(frame, text='File Uploaded Successfully!', font = ("Courier", 10), background="#86acac")
                label.grid(row = 4, column = 0, pady=10)
                screen_7(root, frame, user_choices)
        except Exception: 
                traceback.print_exc()
                messagebox.showerror('pop-up error', "program error: file path is None\nprogram exit" )
                finish_program(root, frame)

def verification_target (user_choices): 
    command_dir = ""
    for choice in user_choices :
        command_dir = command_dir + choice + "/"
    command_dir = command_dir + "target/"
    command = "./program.out 1 " + command_dir
    stream = os.popen(command)
    output = stream.read()
    if "program error" in output:
        messagebox.showerror('pop-up error', str(output))
        finish_program (root, frame)
        return None
    else:
        return command_dir


# Screen 7
def screen_7 (root, old_frame, user_choices):
    old_frame.destroy()

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='Would you like to do:', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    
    button_rg = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Register Activity', command = lambda : screen_8(root, frame, user_choices))
    button_rg.grid(row = 1, column = 0, sticky = W, pady = 2, padx = 10)

    button_an = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Analyze Activities', command = lambda : finish(root, frame))
    button_an.grid(row = 1, column = 0, sticky = E, pady = 2, padx = 10)

# Screen 8
def screen_8 (root, old_frame, user_choices):
    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='What is the activity', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)

    warning = Label(frame, text ='Please, do not use space, or any special caracteres', font = ("Courier", 10), background="#86acac") 
    warning.grid(row = 1, column = 0, sticky = N)

    choice = StringVar(frame, "")
    entry = tk.Entry(frame, textvariable = choice, font=('calibre',10,'normal'))
    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : pop_up_screen_8(choice.get(), user_choices, frame))
    button.grid(row = 3, column = 0, sticky = N, pady = 2, padx = 10)
    entry.grid(row = 2, column = 0, sticky = N, pady = 2, padx = 10, ipady = 5) 

def pop_up_screen_8 (mensagem, user_choices, frame):
    command = "./program.out 6 ../config/activities/"
    for choice in user_choices:
        command = command + choice + "/"
    command = command + mensagem
    stream = os.popen(command)
    output = stream.read()

    if "yes" in output:
        if messagebox.askyesno('pop-up information', 'Activity already registered\nWould you like regiter another way to same activity?') :
            inspect_screen_8 (mensagem, user_choices, frame)
        else :
            if verification (mensagem, user_choices):
                screen_10 (root, frame, user_choices, None, None)
    elif "no" in output:
        inspect_screen_8 (mensagem, user_choices, frame)
    else :
        messagebox.showerror('pop-up error', 'Internal error occur')
        finish_program (root, frame)

def inspect_screen_8 (mensagem, user_choices, frame):
    if verification(mensagem, user_choices) :
        screen_9(root, frame, user_choices)

# Screen 9
def screen_9 (root, old_frame, user_choices):
    old_frame.destroy()
    ck_var = []
    count = 0

    root.grid_rowconfigure(0, weight= 1)
    root.grid_rowconfigure(1, weight= 0)

    label = Label(root, text ='Choice the processor identifiers', font = ("Courier bold", 12), foreground="white", background="#86acac") 
    label.grid(row = 2, column = 1, sticky = "e")

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 2, column = 2, sticky = "sew")
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    button = tk.Button(frame, text = 'Next', font = ("Courier", 12), command = lambda : register_activity(root, frame, ck_var, user_choices, label, v_scroll))
    button.grid(row = 0, column = 1, sticky = "sew")
    button = tk.Button(frame, text = 'Show pIDs choices', font = ("Courier", 12), command = lambda : show_choices(root, frame, ck_var))
    button.grid(row = 0, column = 0, sticky = "sew")

    v_scroll = ScrollableFrame(root)
    v_scroll.grid(row = 0, column = 1, columnspan = 2, sticky = "nsew")

    try:
        file = open("../config/pids/info_file.txt", "r")
    except:
        messagebox.showerror('pop-up error', "program error: Can not create open a file: ../config/pids/info_file.txt\nprogram exit" )

    line = file.readline()
    if line[0] == ">" :
        line = line[1:]
        text_ck_button = line
        line = file.readline()
    else:
        messagebox.showerror('pop-up error', "program error: File with wrong format: ../config/pids/info_file.txt\nprogram exit" )
    
    while line:
        if line[0] == ">" :
            ck_var.append(tk.StringVar(v_scroll, "-1"))
            tk.Checkbutton(v_scroll.scrollable_frame, text = text_ck_button, font = ("Courier", 10), variable = ck_var[count], onvalue = text_ck_button.split(":")[0], offvalue = "-1", background="#86acaf").pack(side = tk.TOP, expand = True, fill = 'both')
            count += 1
            line = line[1:]
            text_ck_button = line
        else:
            text_ck_button = text_ck_button + "\n" + line
        line = file.readline()

#Class ScrollableFrame implementation for:
#https://blog.teclado.com/tkinter-scrollable-frames/
class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        
        canvas = Canvas(self,background="#86acac")
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row = 0, column = 0, sticky = "nsew")
        scrollbar.grid(row = 0, column = 0, sticky = "nsw")

def show_choices(root, frame, ck_var):
    pids = ""
    for var in ck_var:
        var_aux = str(var.get())
        if "-1" not in var_aux:
            pids = pids + var_aux + ","
    pids = pids[:-1]
    messagebox.showinfo('pop-up info', "Selected pIDs:\n" + pids)

def register_activity(root, frame, ck_var, user_choices, label, v_scroll):
    pids = ""
    path = "../config/activities"
    for choice in user_choices:
        path = path + "/" + choice

    for var in ck_var:
        var_aux = str(var.get())
        if "-1" not in var_aux:
            pids = pids + var_aux + ","
    pids = pids[:-1]

    command = "./program.out 4 " + path + " " + pids
    stream = os.popen(command)
    output = stream.read()

    if "program error" in output:
        messagebox.showerror('pop-up error', str(output))
        finish_program(root, frame)
    else:
        screen_10 (root, frame, user_choices, label, v_scroll)

# Screen 10
def screen_10 (root, old_frame, user_choices, old_label, old_v_scroll):
    root.grid_rowconfigure(0, weight= 1)
    root.grid_rowconfigure(1, weight= 0)

    old_frame.destroy()
    if old_label is not None and old_v_scroll is not None:
        old_label.destroy()
        old_v_scroll.destroy()

    path = "../config/activities/"
    for choice in user_choices:
        path = path + choice + "/"

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    frame.grid_rowconfigure(0, weight=0)
    frame.grid_rowconfigure(1, weight=0)
    frame.grid_rowconfigure(2, weight=1)

    label = Label(frame, text ='Activity registered:', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    
    frame_button = tk.LabelFrame(frame, relief = FLAT, background="#86acac")
    frame_button.grid(row = 1, column = 0, sticky = "nsew")
    frame_button.grid_columnconfigure(0, weight=1)
    frame_button.grid_columnconfigure(1, weight=1)

    button_1 = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), text = 'Show dir tree files', command = lambda : list_files(root, frame, path))
    button_1.grid(row = 1, column = 0, sticky = "nsew", pady = 2, padx = 10)

    button_2 = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), text = 'Show dir tree graph', command = lambda : print_activity_paths(path, user_choices))
    button_2.grid(row = 1, column = 1, sticky = "nsew", pady = 2, padx = 10)

    button_3 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Next', command = lambda : finish_program(root, frame))
    button_3.grid(row = 1, column = 1, sticky = "nsew", pady = 2, padx = 10)

def print_activity_paths(path, user_choices):
    names = []
    numbers = []
    edges = []
    flag = 0

    names.append(user_choices[-1])
    numbers.append(flag)
    dir = activity_paths(path, flag, names, numbers, edges)
    graph = Graph(n=dir[0], edges=dir[3], directed=True)
    

    graph.vs["name"] = dir[1]
    graph.vs["label"] = graph.vs["name"]
    graph.es["color"] = ["gray"]
    graph.vs["color"] = ["pink"]
    graph.vs[0]["color"] = "blue"
    graph.vs["font"] = "Courier bold"
    
    for edge in edges:
        if 0 in edge:
            graph.vs[graph.get_eid(edge[0], edge[1]) + 1]["color"] = "lightblue"
    
    visual_style = {}
    visual_style["layout"] = graph.layout_reingold_tilford_circular()
    visual_style["edge_color"] = graph.es["color"]
    visual_style["autocurve"] = False
    visual_style["vertex_size"] = 30
    visual_style["vertex_label_color"] = "black"
    visual_style["vertex_label_dist"] = 2
    visual_style["edge_label_dist"] = -1
    visual_style["edge_curved"] = 0
    visual_style["margin"] = 40

    p = Plot(background=(255,255,255), bbox=(1250, 1250), target=None)
    p.add(graph, **visual_style, bbox=(0,0,1250, 1250), target=None)
    p.show()

def activity_paths(path, flag, names, numbers, edges) :
    command = "ls -l " + path + " | grep ^d | rev | cut -d \" \" -f 1 | rev"
    stream = os.popen(command)
    output = stream.read()

    ret = []
    flag_dir = flag
    dir = ""
    for out in output :
        if "\n" not in out:
            dir = dir + out
        else:
            flag += 1
            names.append(dir)
            numbers.append(flag)
            edge = (flag_dir, flag)
            edges.append(edge)
            new_path = path + dir + "/"

            ret = activity_paths(new_path, flag, names, numbers, edges)
            flag = ret[0]
            names = ret[1]
            numbers  = ret[2]
            edges = ret[3]
            dir = ""
    
    ret = []
    ret.append(flag)
    ret.append(names)
    ret.append(numbers)
    ret.append(edges)
    return ret

#list_files implementation for:
#https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def list_files(root, frame, startpath):
    listbox = Listbox(frame)
    scrollbar = Scrollbar(frame)
    listbox.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew")
    scrollbar.grid(row = 2, column = 0, columnspan = 2, sticky = "nse")

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '', 1).count(os.sep)
        indent = ' ' * 6 * (level)
        txt = str('{}{}/'.format(indent, os.path.basename(root)))
        listbox.insert(END, txt)
        
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)

# Common Analyze Step Function
def verification (mensagem, user_choices): 
    mensagem = str(mensagem.lower())
    msg = "".join(c for c in mensagem if c.isalnum())
    if msg  != "" :
        command_dir = ""
        user_choices.append(msg)
        for choice in user_choices :
            command_dir = command_dir + choice + "/"
        if messagebox.askyesno('pop-up information', 'You select: ' + msg) :
            command = "./program.out 1 " + command_dir
            stream = os.popen(command)
            output = stream.read()

            if "program error" in output:
                messagebox.showerror('pop-up error', str(output))
                finish_program (root, frame)
        return True
    else:
        return False

# Screen 11
def screen_11 (root, old_frame, user_choices):
    old_frame.destroy()

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='Would you like to do:', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    
    button_rg = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Register Activity', command = lambda : finish(root, frame, user_choices))
    button_rg.grid(row = 1, column = 0, sticky = W, pady = 2, padx = 10)

    button_an = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Analyze Activities', command = lambda : finish(root, frame))
    button_an.grid(row = 1, column = 0, sticky = E, pady = 2, padx = 10)


# Doing later
def analyze_step_algorithm (mensagem, user_choices, frame): 
    if verification(mensagem, user_choices) :
        finish_program(root, frame)

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

def finish(root, frame):
    root.destroy()
    '''command = "./program.out 0"
    stream = os.popen(command)
    output = stream.read()
    if "program error" in output:
        #must need to handle with the error, finish the program
        messagebox.showerror('pop-up error', str(output))
        print(str(output))'''



# Execute Tkinter
root.mainloop()
