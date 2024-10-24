from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='purple')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

