from tkinter import Tk, Entry, Button, StringVar

# Define a Calculator class to handle the calculator's GUI and functionality.
class Calculator:
    def __init__(self, master):
        self.configure_window(master)
        self.equation = StringVar()  # StringVar to store and update the equation display.
        self.entry_value = ''  # A string to keep track of the current input.

        # Create display and buttons for the calculator.
        self.create_display(master)
        self.create_buttons(master)

    # Configure the main window's appearance and settings.
    def configure_window(self, master):
        master.title("Calculator")  # Set window title
        master.geometry('357x420+0+0')  # Define window size and initial position.
        master.config(bg='white')  # Set background color to white.
        master.resizable(False, False)  # Prevent resizing to maintain button layout.

    # Create the entry display to show the current equation or result.
    def create_display(self, master):
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), 
              textvariable=self.equation).place(x=0, y=0)
        # The display uses `textvariable=self.equation` to automatically update with equation changes.

    # Define and place the buttons for numbers, operations, and functionality.
    def create_buttons(self, master):
        buttons = [
            ('(', 0, 70), (')', 90, 70), ('%', 180, 70), ('C', 270, 70),
            ('7', 0, 140), ('8', 90, 140), ('9', 180, 140), ('/', 270, 140),
            ('4', 0, 210), ('5', 90, 210), ('6', 180, 210), ('*', 270, 210),
            ('1', 0, 280), ('2', 90, 280), ('3', 180, 280), ('-', 270, 280),
            ('0', 0, 350), ('.', 90, 350), ('+', 180, 350), ('=', 270, 350)
        ]
        
        # Loop through the buttons list and create each button.
        for (text, x, y) in buttons:
            Button(master, text=text, width=11, height=4, relief='flat', bg='white',
                   command=lambda txt=text: self.handle_click(txt)).place(x=x, y=y)
            # Each button triggers `handle_click`, passing the button's text as an argument.

    # Handle button clicks, including numbers, operators, clear, and equals.
    def handle_click(self, value):
        if value == '=':
            self.solve()  # If '=' is clicked, calculate the result.
        elif value == 'C':
            self.clear()  # If 'C' is clicked, clear the display.
        else:
            self.update_entry(value)  # Otherwise, update the entry with the clicked value.

    # Update the entry field with the button's value.
    def update_entry(self, value):
        self.entry_value += str(value)  # Append clicked value to entry_value string.
        self.equation.set(self.entry_value)  # Update the display with the new entry.

    # Clear the entry field and reset `entry_value`.
    def clear(self):
        self.entry_value = ''  # Reset entry_value to an empty string.
        self.equation.set('')  # Clear the display.

    # Evaluate the expression in `entry_value` and display the result.
    def solve(self):
        try:
            result = eval(self.entry_value)  # Calculate the expression in entry_value.
            self.equation.set(result)  # Show result in display.
            self.entry_value = str(result)  # Update entry_value with result for further calculations.
        except Exception:
            self.equation.set("Error")  # Show "Error" if the calculation fails.
            self.entry_value = ''  # Reset entry_value after error.

# Set up and run the main application loop.
root = Tk()
calculator = Calculator(root)  # Create an instance of the Calculator class.
root.mainloop()  # Start the main event loop to keep the GUI running.