from tkinter import *
import tkinter.messagebox
import time
window = Tk()
window.wm_withdraw()

# message at x:200,y:200
#window.geometry("1x1+200+200")  # remember its.geometry("WidthxHeight(+or-)X(+or-)Y")
mes = tkinter.messagebox.showerror(title="error", message="Error Message")

# center screen message
#window.geometry(f"1x1+{round(window.winfo_screenwidth() / 2)}+{round(window.winfo_screenheight() / 2)}")
#tkinter.messagebox.showinfo(title="Greetings", message="Hello World!")