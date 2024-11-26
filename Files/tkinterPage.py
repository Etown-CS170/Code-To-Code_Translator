from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Code-To-Code Translator")

screen_width = str(root.winfo_screenwidth())
screen_height = str(root.winfo_screenheight())

root.geometry(screen_width+"x"+screen_height+"+0+0")
root.iconbitmap('./assets/CodeToCodeTranslate.ico')

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()