import tkinter as tk

window = tk.Tk()
screen_width = window.winfo_screenwidth() 
screen_height = window.winfo_screenheight()
window.attributes('-zoomed', True)
geometry = window.winfo_geometry()
#window.resizable(False, False)
window.title("Android Activities Analyzer")
#greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack(fill="both")
logo = tk.PhotoImage(file="logo.png")
#w1 = logo.subsample(int(screen_width/30), int(screen_width/30))
w2 = tk.Label(window, image=logo).pack(side="top")


w2 = tk.Label(window,justify=tk.LEFT,padx = 10, text="explanation").pack(side="top", anchor = 'center')

window.configure(background="#86acac")
label = tk.Label(text="Hello, Tkinter", fg="black", font = "Verdana 10 bold", bg="#86acac")
#label.pack()
window.mainloop()