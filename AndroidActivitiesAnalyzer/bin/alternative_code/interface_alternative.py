'''  interface.py - Graphic Interface of the Program
 
    Copyright (c) 2022, Garcia M. A. <marilenegarcia@usp.br>

    This file is part of Android Activities Analyzer Program.

    Android Activities Analyzer Program is free software: you 
    can redistribute it and/or modify it under the terms of the 
    GNU General Public License as published by the Free Software 
    Foundation, either version 3 of the License, or (at your option) 
    any later version.
   
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
   
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

#################### Import Modules ###################
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
from igraph import *

################# Building screens #####################

# Screen 0
root = Tk()
path_activity = ""

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

button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Begin', command = lambda : screens_1_2_3_4_5(root, frame))
button.grid(row = 1, column = 0)

# Screens 1,2,3,4,5
def screens_1_2_3_4_5 (root, old_frame):
    command = "./program.out 0"
    stream = os.popen(command)
    output = stream.read()
    if "program error" in output:
        messagebox.showerror('pop-up error', str(output))
        finish (root, old_frame)

    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='Insert the Activity Path', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)

    warning = Label(frame, text ='Please, insert following the model: dir_name_1/dir_name_2 ', font = ("Courier", 10), background="#86acac") 
    warning.grid(row = 1, column = 0, sticky = N)

    warning = Label(frame, text ='It will be save inside ../../config/activities/', font = ("Courier", 10), background="#86acac") 
    warning.grid(row = 2, column = 0, sticky = N)

    choice = StringVar(frame, "")
    entry = tk.Entry(frame, textvariable = choice, font=('calibre',10,'normal'))
    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : inspect_screens_1_2_3_4_5(choice.get(), frame))
    button.grid(row = 4, column = 0, sticky = N, pady = 2, padx = 10)
    entry.grid(row = 3, column = 0, sticky = N, pady = 2, padx = 10, ipady = 5)  
    
def inspect_screens_1_2_3_4_5 (usr_path, frame): 
    if verification(usr_path):
        dir = verification_target()
        screen_6(root, frame, dir)
    else:
        messagebox.showerror('pop-up error', "Something goes wrong")
        finish_program (root, frame)


# Screen 6
def screen_6 (root, old_frame, dir):
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

    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Choose File', command = lambda : open_file(root, frame, dir))
    button.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10)

def open_file(root, frame, dir):
    file_path = filedialog.askopenfile(mode='r', filetypes=[('Text files', '*txt')])
    if file_path is not None:
        try:
            copy(file_path.name, "../../config/pids/logs.txt")
            copy(file_path.name, "../../config/activities/" + dir + "target.txt")
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
                frame.update_idletasks()
                time.sleep(0.5)
                pb.destroy()
                label = Label(frame, text='File Uploaded Successfully!', font = ("Courier", 10), background="#86acac")
                label.grid(row = 4, column = 0, pady=10)
                screen_7(root, frame)
        except Exception: 
                traceback.print_exc()
                messagebox.showerror('pop-up error', "program error: file path is None\nprogram exit" )
                finish_program(root, frame)

# Screen 7
def screen_7 (root, old_frame):
    old_frame.destroy()

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = "nsew")
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='Would you like to do:', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = "nsew", ipady = 10)
    
    frame_button = tk.LabelFrame(frame, relief = FLAT, background="#86acac")
    frame_button.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew")

    button_rg = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), text = 'Register Activity', command = lambda : screen_8(root, frame))
    button_rg.grid(row = 1, column = 0, sticky = "nsew", pady = 2, padx = 10)

    button_an = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), text = 'Analyze Activities', command = lambda : screen_11(root, frame))
    button_an.grid(row = 1, column = 1, sticky = "nsew", pady = 2, padx = 10)

# Screen 8
def screen_8 (root, old_frame):
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
    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : pop_up_screen_8(choice.get(), frame))
    button.grid(row = 3, column = 0, sticky = N, pady = 2, padx = 10)
    entry.grid(row = 2, column = 0, sticky = N, pady = 2, padx = 10, ipady = 5) 

def pop_up_screen_8 (mensagem, frame):
    global path_activity
    command = "./program.out 6 "+ path_activity + mensagem
    print(command)
    stream = os.popen(command)
    output = stream.read()

    if "yes" in output:
        if messagebox.askyesno('pop-up information', 'Activity already registered\nWould you like regiter another way to same activity?') :
            inspect_screen_8 (mensagem, frame)
        else :
            if verification (mensagem):
                screen_10 (root, frame, None, None)
            else:
                messagebox.showerror('pop-up error', 'Internal error occur')
                finish(root, frame)
    elif "no" in output:
        inspect_screen_8 (mensagem, frame)
    else :
        messagebox.showerror('pop-up error', 'Internal error occur')
        finish_program (root, frame)

def inspect_screen_8 (mensagem, frame):
    if verification(mensagem) :
        screen_9(root, frame)
    else:
        messagebox.showerror('pop-up error', 'Internal error occur')
        finish(root, frame)

# Screen 9
def screen_9 (root, old_frame):
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
    button = tk.Button(frame, text = 'Next', font = ("Courier", 12), command = lambda : register_activity(root, frame, ck_var, label, v_scroll))
    button.grid(row = 0, column = 1, sticky = "sew")
    button = tk.Button(frame, text = 'Show pIDs choices', font = ("Courier", 12), command = lambda : show_choices(root, frame, ck_var))
    button.grid(row = 0, column = 0, sticky = "sew")

    v_scroll = ScrollableFrame(root)
    v_scroll.grid(row = 0, column = 1, columnspan = 2, sticky = "nsew")

    try:
        file = open("../../config/pids/info_file.txt", "r")
    except:
        messagebox.showerror('pop-up error', "program error: Can not create open a file: ../../config/pids/info_file.txt\nprogram exit" )
        finish_program (root, frame)

    line = file.readline()
    if line[0] == ">" :
        line = line[1:]
        text_ck_button = line
        line = file.readline()
    else:
        messagebox.showerror('pop-up error', "program error: File with wrong format: ../../config/pids/info_file.txt\nprogram exit" )
        finish_program (root, frame)
    
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

def register_activity(root, frame, ck_var, label, v_scroll):
    pids = ""
    global path_activity
    path = "../../config/activities/" + path_activity

    print("path" + path)
    for var in ck_var:
        var_aux = str(var.get())
        if "-1" not in var_aux:
            pids = pids + var_aux + ","
    pids = pids[:-1]
    
    if(pids != ""):
        command = "./program.out 4 " + path + " " + pids
        stream = os.popen(command)
        output = stream.read()

        if "program error" in output:
            messagebox.showerror('pop-up error', str(output))
            finish_program(root, frame)
        else:
            screen_10 (root, frame, label, v_scroll)
    else:
        messagebox.showwarning('pop-up warning', 'Please, select at least one pid')


# Screen 10
def screen_10 (root, old_frame, old_label, old_v_scroll):
    root.grid_rowconfigure(0, weight= 1)
    root.grid_rowconfigure(1, weight= 0)
    global path_activity

    old_frame.destroy()
    if old_label is not None and old_v_scroll is not None:
        old_label.destroy()
        old_v_scroll.destroy()

    path = "../../config/activities/" + path_activity

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

    button_2 = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), text = 'Show dir tree graph', command = lambda : print_activity_paths(path))
    button_2.grid(row = 1, column = 1, sticky = "nsew", pady = 2, padx = 10)

    button_3 = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Next', command = lambda : finish_program(root, frame))
    button_3.grid(row = 1, column = 1, sticky = "nsew", pady = 2, padx = 10)

# Screen 11
def screen_11 (root, old_frame, user_choices):
    old_frame.destroy()

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    label = Label(frame, text ='Searching for match activities:', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    log_file = StringVar(frame, "")

    warning = Label(frame, text ='the search happens in all registered activities of this path*', font = ("Courier", 10), background="#86acac") 
    warning.grid(row = 1, column = 0, sticky = NE)

    button = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Start search', command = lambda : screen_11_search(root, frame, user_choices))
    button.grid(row = 2, column = 0, sticky = NW, pady = 2, padx = 10)

    print = user_choices

def screen_11_search(root, frame, user_choices):
    path = "../../config/activities/"
    for choice in user_choices:
        path = path + choice + "/"

    pb = Progressbar(frame, orient=HORIZONTAL, length=300, mode='determinate')
    pb.grid(row = 4, column = 0, pady=20)
    for i in range(4):
        frame.update_idletasks()
        pb['value'] += 20
        time.sleep(0.5)

    command = "./program.out 5 " + path
    stream = os.popen(command)
    output = stream.read()

    path_2 = "../../results/"
    command_2 = "ls -l " + path_2 + " | grep ^d | wc -l"
    stream_2 = os.popen(command_2)
    output_2 = stream_2.read()

    if "program error" in output:
        if messagebox.askyesno('pop-up information', 'There is no registered activity in: ' + path + '\nWould you like register this one?'):
            screen_8(root, frame, user_choices)
        else:
            finish_program(root, frame)
    
    elif "0" in output_2:
        if messagebox.askyesno('pop-up information', 'There is no match activity in: ' + path + '\nWould you like register this logs as a new activity?'):
            screen_8(root, frame, user_choices)
        else:
            finish_program(root, frame)
    else:
        frame.update_idletasks()
        pb['value'] += 20
        time.sleep(1)
        frame.update_idletasks()
        time.sleep(0.5)
        pb.destroy()
        screen_12(root, frame, user_choices)

# Screen 12
def screen_12 (root, old_frame, user_choices):
    old_frame.destroy()

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    frame.grid_rowconfigure(0, weight=0)
    frame.grid_rowconfigure(1, weight=0)
    frame.grid_rowconfigure(2, weight=1)

    label = Label(frame, text ='Match Activities:', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)
    
    listbox = tk.Listbox(frame)
    scrollbar = Scrollbar(frame)
    listbox.grid(row = 2, column = 0, columnspan = 1, sticky = "nsew")
    scrollbar.grid(row = 2, column = 0, columnspan = 1, sticky = "nse")

    file = open("../../results/results.txt", "r")
    line_number = 0
    click_lines = []
    for line in file:
        line = line. rstrip('\n')
        if "config" in line:
            listbox.insert(line_number, line)
            line_number += 1
        elif "match" in line:
            listbox.insert(line_number, line.split(" is")[0])
            listbox.itemconfig(line_number, {'bg':'green', 'fg':'white'})
            click_lines.append(line_number)
            line_number += 1
        elif "%" in line:
            listbox.insert(line_number, line)
            listbox.itemconfig(line_number, {'fg':'green'})
            line_number += 1
    file.close()
    
    label_select = Label(frame, text ='Click and select a line for more details', font = ("Courier", 18), background="#86acac") 
    label_select.grid(row = 3, column = 0, sticky = N, ipady = 10)

    warning = Label(frame, text ='only the lines with background green are available to be select*', font = ("Courier", 10), background="#86acac") 
    warning.grid(row = 4, column = 0, sticky = NE)

    button_select = tk.Button(frame, background="#86acac", font = ("Courier", 14), text = 'Select', command = lambda : verification_screen_12(root, frame, user_choices, click_lines, listbox.curselection(), listbox))
    button_select.grid(row = 5, column = 0, sticky = "nsew", pady = 2, padx = 10)
    
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)

def verification_screen_12 (root, frame, user_choices, right_lines, select_line, listbox):
    if select_line != ():
        if select_line[0] in right_lines:
            message = listbox.get(select_line[0])
            if messagebox.askyesno('pop-up information', 'You select:\n' + message):
                screen_13(root, frame, user_choices, message)
            else:
                screen_12(root, frame, user_choices)
        else:
            messagebox.showwarning('pop-up warning', 'Please, select a line with green background')
            screen_12(root, frame, user_choices)

# Screen 13
def screen_13 (root, old_frame, user_choices, message):
    old_frame.destroy()
    root.grid_rowconfigure(0, weight= 1)
    root.grid_rowconfigure(1, weight= 0)

    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    frame.grid_rowconfigure(0, weight=0)
    frame.grid_rowconfigure(1, weight=0)
    frame.grid_rowconfigure(2, weight=0)
    frame.grid_rowconfigure(3, weight=1)

    label = Label(frame, text ='Match Activities:', font = ("Courier", 18), background="#86acac") 
    label.grid(row = 0, column = 0, sticky = N, ipady = 10)

    frame_button = tk.LabelFrame(frame, relief = FLAT, background="#86acac")
    frame_button.grid(row = 1, column = 0, sticky = "nsew")
    frame_button.grid_columnconfigure(0, weight=1)
    frame_button.grid_columnconfigure(1, weight=1)

    label_1 = Label(frame_button, text ='*filtro unique lines', font = ("Courier", 10), background="#86acac") 
    label_1.grid(row = 2, column = 0, sticky = NW, ipady = 10)
    button_1 = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), width=20, text = 'Filter 1', command = lambda : screen_13_scroll (root, frame, user_choices, message, 0))
    button_1.grid(row = 1, column = 0, sticky = NW, pady = 2, padx = 5)

    label_2 = Label(frame_button, text ='*filtro unique lines\n without consider hexadecimal values', font = ("Courier", 10), background="#86acac") 
    label_2.grid(row = 2, column = 1, sticky = NW, ipady = 10)
    button_2 = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), width=20, text = 'Filter 2', command = lambda : screen_13_scroll (root, frame, user_choices, message, 1))
    button_2.grid(row = 1, column = 1, sticky = NW, pady = 2, padx = 5)

    label_3 = Label(frame_button, text ='*filtro unique lines\n without consider numerical values', font = ("Courier", 10), background="#86acac") 
    label_3.grid(row = 2, column = 2, sticky = NW, ipady = 10)
    button_3 = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), width=20, text = 'Filter 3', command = lambda : screen_13_scroll (root, frame, user_choices, message, 2))
    button_3.grid(row = 1, column = 2, sticky = NW, pady = 2, padx = 5)

    button_4 = tk.Button(frame, background="#86acac", font = ("Courier", 14), width=20, text = 'Next', command = lambda : finish_program (root, frame))
    button_4.grid(row = 1, column = 1, sticky = N, pady = 2, padx = 5)

    button_5 = tk.Button(frame, background="#86acac", font = ("Courier", 14), width=20, text = 'Back', command = lambda : screen_12 (root, frame, user_choices))
    button_5.grid(row = 2, column = 1, sticky = N, pady = 2, padx = 5)

def screen_13_scroll (root, frame, user_choices, str, button):
    str = str.replace(" ", "")
    str = str.split(":")
    dir = "../../results/" + str[0] + "/" + str[1] + "/"
    files = ["unique_umatch_lines.txt", "unique_umatch_lines_no_hex.txt", "unique_umatch_lines_no_numbers.txt"]
    dir = dir + files[button]

    listbox = Listbox(frame)
    scrollbar = Scrollbar(frame)
    listbox.grid(row = 3, column = 0, sticky = "nsew")
    scrollbar.grid(row = 3, column = 0, sticky = "nse")

    num_lines = sum(1 for lines in open(dir))
    line_number = 0

    file = open(dir, "r")
    if(num_lines == 0):
        listbox.insert(0, "There is no unmatch lines in activity...")
    elif(num_lines < 1000):
        for line in file:
            line = line.rstrip('\n')
            if  line.startswith('E'):
                listbox.insert(line_number, line)
                listbox.itemconfig(line_number, {'fg':'red'})
                line_number += 1
            elif line.startswith('W'):
                listbox.insert(line_number, line)
                listbox.itemconfig(line_number, {'fg':'orange'})
                line_number += 1
            elif line.startswith('I'):
                listbox.insert(line_number, line)
                listbox.itemconfig(line_number, {'fg':'blue'})
                line_number += 1
            elif line.startswith('D'):
                listbox.insert(line_number, line)
                listbox.itemconfig(line_number, {'fg':'purple'})
                line_number += 1
            elif line.startswith('V'):
                listbox.insert(line_number, line)
                listbox.itemconfig(line_number, {'fg':'green'})
                line_number += 1
            else:
                listbox.insert(line_number, line)
                line_number += 1
    else:
        os.system("gedit " + dir)
        listbox.insert(0, "Maximum file size exceeded")
        listbox.insert(1, "Opening the file in gedit...")

    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
    file.close()

# Screen 14
def finish_program (root, old_frame):
    old_frame.destroy()
    frame = tk.LabelFrame(root, relief = FLAT, background="#86acac")
    frame.grid(row = 0, column = 1, columnspan = 2, sticky = tk.NSEW)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    frame_button = tk.LabelFrame(frame, relief = FLAT, background="#86acac")
    frame_button.grid(row = 1, column = 0, sticky = "nsew")

    button = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), text = 'Finish program', command = lambda : finish(root, frame))
    button.grid(row = 1, column = 0, sticky = NE, pady = 2, padx = 10)

    button = tk.Button(frame_button, background="#86acac", font = ("Courier", 14), text = 'Return to begin', command = lambda : screen_1 (root, frame))
    button.grid(row = 1, column = 1, sticky = NW, pady = 2, padx = 10)

def finish(root, frame):
    root.destroy()


# Auxiliar Functions
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
def verification (usr_path):
    position = 0
    char_deleted = 0

    global path_activity
    usr_path = str(usr_path.lower())
    usr_path = usr_path.replace(" ", "")
    
    while(position < len(usr_path) - 1 and usr_path[position] == "/"):
        usr_path = usr_path[1:]

    path_activity = path_activity + usr_path
    
    while(position < len(usr_path) - 1):
        if (usr_path[position] == "/"):
            if(usr_path[position+1] == "/"):
                flag = 1
                while(usr_path[position+flag] == "/" and position + flag < len(usr_path) - 1):
                    flag += 1
                flag -= 1
                path_activity = path_activity[:position - char_deleted] + path_activity[position - char_deleted + flag:]
                position = position + flag
                char_deleted = char_deleted + flag
        position += 1

    if(usr_path[position] != "/"):
        path_activity = path_activity + "/"
    elif(usr_path[position - 1] == "/"):
        path_activity = path_activity[:len(path_activity) - 1]

    if usr_path  != "" :
        command = "./program.out 1 " + path_activity
        print("p1"+command)
        stream = os.popen(command)
        output = stream.read()

        if "program error" in output:
            messagebox.showerror('pop-up error', str(output))
            finish_program (root, frame)
            return False
        else:
            messagebox.showinfo('pop-up info', "The activity will be register in ../../config/activities/"+path_activity)
        return True
    else:
        return False

def verification_target (): 
    global path_activity
    print(path_activity)

    command_dir = path_activity + "target/"
    command = "./program.out 1 " + command_dir
    stream = os.popen(command)
    output = stream.read()
    if "program error" in output:
        messagebox.showerror('pop-up error', str(output))
        finish_program (root, frame)
        return None
    else:
        return command_dir

def print_activity_paths(path):
    names = []
    numbers = []
    edges = []
    flag = 0

    names.append(path.split("/")[-1])
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

    p = Plot("graph.png", background=(255,255,255), bbox=(1250, 1250))
    p.add(graph, **visual_style, bbox=(0,0,1250, 1250))
    
    p.show()


# Execute Tkinter
root.mainloop()
