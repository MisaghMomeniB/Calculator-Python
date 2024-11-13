__Hello My Friend 👋🏻__ <br>
__I'm Misagh and I'm Glad You're Here 😉__

# Calculator-Python🐍
I Developed a Calculator  Using __Python__. This Calculator is Simple and Performs Only Basic Operations, Such as ***Addition***, ***Subtraction***, ***Division***, ***Multiplication***, and So on.

I Created Its Graphical Interface Using __Tkinter__ to Provide a Better User Experience.

# Does It Require Any Installation Steps or Prerequisites?
There’s No Need to Install Any __Libraries__ or Set Up a Specific Environment. You Just Need to Import the Core ***Tkinter*** Library and Start Coding in Your Programming Environment.

# Line-by-line Code Analysis

Here is a detailed line-by-line explanation of the provided code for the `Calculator` class, including its GUI and functionality setup using Tkinter in Python:

---

### Importing Necessary Modules

```python
from tkinter import Tk, Entry, Button, StringVar
```

- Imports the `Tk`, `Entry`, `Button`, and `StringVar` classes from the `tkinter` library, which is Python’s standard library for creating GUI applications.
- `Tk` is used to create the main application window.
- `Entry` creates a single-line text box to display the calculator’s equation and results.
- `Button` is used to create buttons for the calculator’s interface.
- `StringVar` is a Tkinter variable type that dynamically updates the entry field when its value is changed.

---

### Defining the Calculator Class

```python
class Calculator:
```

- Defines a class named `Calculator` that will handle the GUI layout and logic for this calculator app.

---

### `__init__` Method

```python
    def __init__(self, master):
```

- This is the constructor method of the `Calculator` class, which is automatically called when an instance of `Calculator` is created.
- It initializes key variables, configures the window, and creates GUI components like the display and buttons.

---

#### Setting Up the Calculator Window

```python
        self.configure_window(master)
```

- Calls the `configure_window` method to set up the main window’s appearance and behavior.

#### Setting Up Calculator Display and Initial Values

```python
        self.equation = StringVar()
        self.entry_value = ''
```

- `self.equation` is a `StringVar` instance, which will dynamically update the calculator’s entry display with each change.
- `self.entry_value` is a plain string to store the current input string, which allows appending of numbers and operators before final evaluation.

---

#### Creating Display and Buttons

```python
        self.create_display(master)
        self.create_buttons(master)
```

- Calls the `create_display` and `create_buttons` methods to add the calculator’s display and buttons to the GUI.

---

### Window Configuration: `configure_window`

```python
    def configure_window(self, master):
```

- This method sets up the main window’s properties like title, size, background color, and resize restrictions.

```python
        master.title("Calculator")
```

- Sets the title of the window to "Calculator."

```python
        master.geometry('357x420+0+0')
```

- Defines the initial size of the window as 357 pixels wide and 420 pixels high, positioned at the top-left corner of the screen (`+0+0`).

```python
        master.config(bg='white')
```

- Sets the background color of the main window to white.

```python
        master.resizable(False, False)
```

- Disables window resizing, which keeps the buttons’ layout fixed.

---

### Creating Display: `create_display`

```python
    def create_display(self, master):
```

- This method creates the entry field to show the current equation or result.

```python
        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)
```

- Creates an `Entry` widget with:
  - `width=17`: Width of the entry field.
  - `bg='#fff'`: White background for the entry.
  - `font=('Arial Bold', 28)`: Uses bold Arial font with size 28 for clear visibility.
  - `textvariable=self.equation`: Binds the entry to `self.equation`, so any change in `self.equation` will update the display.
- `.place(x=0, y=0)`: Positions the entry field at the top-left corner (0, 0).

---

### Creating Buttons: `create_buttons`

```python
    def create_buttons(self, master):
```

- This method defines and arranges all calculator buttons in a grid layout, including numbers, operators, and functions like `C` and `=`.
  
```python
        buttons = [
            ('(', 0, 70), (')', 90, 70), ('%', 180, 70), ('C', 270, 70),
            ('7', 0, 140), ('8', 90, 140), ('9', 180, 140), ('/', 270, 140),
            ('4', 0, 210), ('5', 90, 210), ('6', 180, 210), ('*', 270, 210),
            ('1', 0, 280), ('2', 90, 280), ('3', 180, 280), ('-', 270, 280),
            ('0', 0, 350), ('.', 90, 350), ('+', 180, 350), ('=', 270, 350)
        ]
```

- Creates a list of tuples representing button labels and their positions on the screen. Each tuple has:
  - `text`: Button label.
  - `x`: X-coordinate position.
  - `y`: Y-coordinate position.

---

#### Loop to Create Buttons

```python
        for (text, x, y) in buttons:
            Button(master, text=text, width=11, height=4, relief='flat', bg='white',
                   command=lambda txt=text: self.handle_click(txt)).place(x=x, y=y)
```

- Loops over each button in the `buttons` list and creates a `Button` widget with:
  - `text=text`: The button’s label.
  - `width=11`, `height=4`: Button dimensions.
  - `relief='flat'`: Flat design style.
  - `bg='white'`: White background.
  - `command=lambda txt=text: self.handle_click(txt)`: Sets the button’s command to `handle_click`, passing the button text as an argument.
- `.place(x=x, y=y)`: Places each button at the specified (x, y) coordinates.

---

### Handling Button Clicks: `handle_click`

```python
    def handle_click(self, value):
```

- This method processes the actions based on the button that was clicked. It takes `value` as an argument, representing the button label.

```python
        if value == '=':
            self.solve()
```

- If the `=` button is clicked, it calls the `solve` method to evaluate the current equation.

```python
        elif value == 'C':
            self.clear()
```

- If the `C` button is clicked, it calls the `clear` method to reset the entry field.

```python
        else:
            self.update_entry(value)
```

- For all other buttons (numbers and operators), it calls `update_entry` to add the value to the current equation.

---

### Updating Entry: `update_entry`

```python
    def update_entry(self, value):
```

- This method appends the clicked button’s `value` to `self.entry_value` and updates the display.

```python
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
```

- Adds `value` to `self.entry_value` and updates `self.equation`, so the entry field displays the new equation.

---

### Clearing the Entry: `clear`

```python
    def clear(self):
```

- Clears the current input and resets the display.

```python
        self.entry_value = ''
        self.equation.set('')
```

- Resets `self.entry_value` to an empty string and clears `self.equation`, updating the entry field.

---

### Solving the Equation: `solve`

```python
    def solve(self):
```

- This method evaluates the current equation stored in `self.entry_value`.

```python
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''
```

- Uses `eval` to evaluate `self.entry_value` as a Python expression.
- If evaluation succeeds, `result` is displayed and stored for further calculations.
- If an error occurs (e.g., invalid syntax), it displays "Error" and clears `self.entry_value`.

---

### Running the Application

```python
root = Tk()
calculator = Calculator(root)
root.mainloop()
```

- Creates the main application window (`root`) and initializes the `Calculator` class, setting up the GUI.
- `root.mainloop()` starts the Tkinter event loop, keeping the GUI running until the window is closed.
