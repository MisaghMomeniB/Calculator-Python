from tkinter import Tk, Entry, Button, StringVar, Label, Frame
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
        """Configure the main window settings."""
        master.title("Calculator")
        master.geometry('400x650')
        master.config(bg='#f0f0f0')
        master.resizable(False, False)

    def create_display(self, master):
        """Create the input display for the calculator."""
        self.entry_frame = Frame(master, bg='#f0f0f0')
        self.entry_frame.pack(pady=10)

        self.entry = Entry(
            self.entry_frame,
            width=17,
            bg='#e6e6e6',
            font=('Arial Bold', 28),
            textvariable=self.equation,
            borderwidth=5,
            relief='ridge'
        )
        self.entry.pack()
        self.entry.bind('<Key>', self.keyboard_input)

    def create_history_display(self, master):
        """Create the history display for the calculator."""
        self.history_label = Label(
            master,
            text="History:",
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        self.history_label.pack(pady=10)

        self.history_box = Label(
            master,
            text="",
            font=('Arial', 10),
            justify='left',
            anchor='w',
            bg='#fff',
            borderwidth=2,
            relief='sunken',
            height=5
        )
        self.history_box.pack(padx=10, pady=5, fill='both')

    def create_buttons(self, master):
        """Create buttons for the calculator."""
        button_frame = Frame(master, bg='#f0f0f0')
        button_frame.pack(pady=10)

        buttons = [
            ('(', ')', '%', 'C'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '+', '='),
            ('sin', 'cos', 'tan', 'log'),
            ('π', 'e', '^', '√')
        ]

        for row in buttons:
            button_row = Frame(button_frame, bg='#f0f0f0')
            button_row.pack(side='top', fill='both')

            for text in row:
                Button(
                    button_row,
                    text=text,
                    width=10,
                    height=2,
                    relief='raised',
                    bg='#d1d1d1',
                    command=lambda txt=text: self.handle_click(txt)
                ).pack(side='left', padx=5, pady=5)

    def handle_click(self, value):
        """Handle button clicks and update the calculator state."""
        try:
            if value == '=':
                self.solve()
            elif value == 'C':
                self.clear()
            elif value == 'π':
                self.update_entry(math.pi)
            elif value == 'e':
                self.update_entry(math.e)
            elif value in ['sin', 'cos', 'tan', 'log']:
                self.update_entry(f"{value}(")
            elif value == '√':
                self.update_entry('sqrt(')
            elif value == '^':
                self.update_entry('**')
            else:
                self.update_entry(value)
        except Exception as e:
            self.equation.set("Error")

    def update_entry(self, value):
        """Update the entry field with the given value."""
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        """Clear the calculator display."""
        self.entry_value = ''
        self.equation.set('')

    def solve(self):
        """Evaluate the current expression and display the result."""
        try:
            # Replace mathematical functions with their Python equivalents
            expression = self.entry_value.replace('sin', 'math.sin') \
                                         .replace('cos', 'math.cos') \
                                         .replace('tan', 'math.tan') \
                                         .replace('log', 'math.log10') \
                                         .replace('sqrt', 'math.sqrt')

            # Evaluate the expression
            result = eval(expression)

            # Format the result to avoid excessive decimal places
            formatted_result = "{:,}".format(round(result, 10))
            self.equation.set(formatted_result)

            # Update history
            self.history.append(f"{self.entry_value} = {formatted_result}")
            self.update_history()

            # Reset entry value to the result
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

    def update_history(self):
        """Update the history display with the latest calculations."""
        history_text = "\n".join(self.history[-5:])  # Show only the last 5 entries
        self.history_box.config(text=history_text)

    def keyboard_input(self, event):
        """Handle keyboard input for the calculator."""
        key = event.char

        # Handle numeric and operator keys
        if key.isdigit() or key in '().+-*/%^.':
            self.update_entry(key)

        # Handle Enter key (evaluate expression)
        elif key == '\r':
            self.solve()

        # Handle Backspace key (delete last character)
        elif key == '\x08' and self.entry_value:
            self.entry_value = self.entry_value[:-1]
            self.equation.set(self.entry_value)

        # Handle Clear (C) key
        elif key.lower() == 'c':
            self.clear()


# Application entry point
if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()