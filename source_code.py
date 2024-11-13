from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        self.configure_window(master)
        self.equation = StringVar()
        self.entry_value = ''
        
        self.create_display(master)
        self.create_buttons(master)

    def configure_window(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='white')
        master.resizable(False, False)

    def create_display(self, master):
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), 
              textvariable=self.equation).place(x=0, y=0)

    def create_buttons(self, master):
        buttons = [
            ('(', 0, 70), (')', 90, 70), ('%', 180, 70), ('C', 270, 70),
            ('7', 0, 140), ('8', 90, 140), ('9', 180, 140), ('/', 270, 140),
            ('4', 0, 210), ('5', 90, 210), ('6', 180, 210), ('*', 270, 210),
            ('1', 0, 280), ('2', 90, 280), ('3', 180, 280), ('-', 270, 280),
            ('0', 0, 350), ('.', 90, 350), ('+', 180, 350), ('=', 270, 350)
        ]
        
        for (text, x, y) in buttons:
            Button(master, text=text, width=11, height=4, relief='flat', bg='white',
                   command=lambda txt=text: self.handle_click(txt)).place(x=x, y=y)

    def handle_click(self, value):
        if value == '=':
            self.solve()
        elif value == 'C':
            self.clear()
        else:
            self.update_entry(value)

    def update_entry(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set('')

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()