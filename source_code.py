from tkinter import Tk, Entry, Button, StringVar, Label
import math

class Calculator:
    def __init__(self, master):
        self.configure_window(master)
        self.equation = StringVar()
        self.entry_value = ''
        self.history = []

        self.create_display(master)
        self.create_buttons(master)
        self.create_history_display(master)

    def configure_window(self, master):
        master.title("Calculator")
        master.geometry('400x600')
        master.config(bg='white')
        master.resizable(False, False)

    def create_display(self, master):
        self.entry = Entry(master, width=17, bg='#fff', font=('Arial Bold', 28),
                           textvariable=self.equation)
        self.entry.place(x=0, y=0)
        self.entry.bind('<Key>', self.keyboard_input)

    def create_history_display(self, master):
        self.history_label = Label(master, text="History:", font=('Arial', 12))
        self.history_label.place(x=0, y=450)
        self.history_box = Label(master, text="", font=('Arial', 10), justify='left', anchor='w', bg='white')
        self.history_box.place(x=0, y=480, width=400, height=100)

    def create_buttons(self, master):
        buttons = [
            ('(', 0, 70), (')', 90, 70), ('%', 180, 70), ('C', 270, 70),
            ('7', 0, 140), ('8', 90, 140), ('9', 180, 140), ('/', 270, 140),
            ('4', 0, 210), ('5', 90, 210), ('6', 180, 210), ('*', 270, 210),
            ('1', 0, 280), ('2', 90, 280), ('3', 180, 280), ('-', 270, 280),
            ('0', 0, 350), ('.', 90, 350), ('+', 180, 350), ('=', 270, 350),
            ('sin', 0, 420), ('cos', 90, 420), ('tan', 180, 420), ('log', 270, 420),
            ('π', 0, 490), ('e', 90, 490), ('^', 180, 490), ('√', 270, 490)
        ]
        for (text, x, y) in buttons:
            Button(master, text=text, width=11, height=2, relief='flat', bg='white',
                   command=lambda txt=text: self.handle_click(txt)).place(x=x, y=y)

    def handle_click(self, value):
        if value == '=':
            self.solve()
        elif value == 'C':
            self.clear()
        elif value == 'π':
            self.update_entry(math.pi)
        elif value == 'e':
            self.update_entry(math.e)
        elif value == 'sin':
            self.update_entry('sin(')
        elif value == 'cos':
            self.update_entry('cos(')
        elif value == 'tan':
            self.update_entry('tan(')
        elif value == 'log':
            self.update_entry('log(')
        elif value == '√':
            self.update_entry('sqrt(')
        elif value == '^':
            self.update_entry('**')
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
            expression = self.entry_value.replace('sin', 'math.sin')\
                                         .replace('cos', 'math.cos')\
                                         .replace('tan', 'math.tan')\
                                         .replace('log', 'math.log10')\
                                         .replace('sqrt', 'math.sqrt')
            result = eval(expression)
            result = "{:,}".format(round(result, 10))
            self.equation.set(result)
            self.history.append(f"{self.entry_value} = {result}")
            self.update_history()
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

    def update_history(self):
        # Ensure history is displayed correctly with line breaks
        history_text = "\n".join(self.history[-5:])
        self.history_box.config(text=history_text)

    def keyboard_input(self, event):
        key = event.char
        if key.isdigit() or key in '().+-*/%^.':
            self.update_entry(key)
        elif key == '\r':
            self.solve()
        elif key == '\x08' and self.entry_value:
            self.entry_value = self.entry_value[:-1]
            self.equation.set(self.entry_value)
        elif key.lower() == 'c':
            self.clear()

root = Tk()
calculator = Calculator(root)
root.mainloop()