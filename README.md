__Hello My Friend 👋🏻__ <br>
__I'm Misagh and I'm Glad You're Here 😉__

# Calculator-Python🐍
I Developed a Calculator  Using __Python__. This Calculator is Simple and Performs Only Basic Operations, Such as ***Addition***, ***Subtraction***, ***Division***, ***Multiplication***, and So on.

I Created Its Graphical Interface Using __Tkinter__ to Provide a Better User Experience.

# Does It Require Any Installation Steps or Prerequisites?
There’s No Need to Install Any __Libraries__ or Set Up a Specific Environment. You Just Need to Import the Core ***Tkinter*** Library and Start Coding in Your Programming Environment.

# Line-by-line Code Analysis

```python
from tkinter import Tk, Entry, Button, StringVar
```
- **Importing Modules**: This line imports essential components from the `tkinter` library. `Tk` is the main window class, `Entry` is a widget for user input, `Button` is for creating buttons, and `StringVar` is a variable class that helps manage string variables in Tkinter.

```python
class Calculator:
```
- **Class Definition**: This line defines a new class called `Calculator`. A class is a blueprint for creating objects that can encapsulate data and functionality.

```python
def __init__(self, master):
```
- **Constructor Method**: This method initializes the `Calculator` class. The `master` parameter represents the main window in which the calculator will be displayed.

```python
master.title("Calculator")
```
- **Set Window Title**: This sets the title of the main window to "Calculator".

```python
master.geometry('357x420+0+0')
```
- **Set Window Size and Position**: This line defines the dimensions of the window as 357 pixels wide and 420 pixels tall, positioned at (0, 0) on the screen.

```python
master.config(bg='purple')
```
- **Set Background Color**: This sets the background color of the window to purple.

```python
master.resizable(False, False)
```
- **Disable Resizing**: This prevents the user from resizing the window, keeping the defined dimensions intact.

```python
self.equation = StringVar()
self.entry_value = ''
```
- **String Variable and Entry Value**: `self.equation` is a `StringVar` that will hold the current expression entered by the user. `self.entry_value` is an empty string that will build the equation as buttons are pressed.

```python
Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)
```
- **Entry Widget**: This line creates an input field (Entry widget) for displaying the equation. It has a width of 17 characters, a white background, a bold Arial font size of 28, and it is bound to `self.equation`. The `place` method positions it at coordinates (0, 0).

```python
buttons = [
    ('(', 0, 70), (')', 90, 70), ('%', 180, 70), ('C', 270, 70),
    ('7', 0, 140), ('8', 90, 140), ('9', 180, 140), ('/', 270, 140),
    ('4', 0, 210), ('5', 90, 210), ('6', 180, 210), ('*', 270, 210),
    ('1', 0, 280), ('2', 90, 280), ('3', 180, 280), ('-', 270, 280),
    ('0', 0, 350), ('.', 90, 350), ('+', 180, 350), ('=', 270, 350)
]
```
- **Button Layout**: This creates a list of tuples that define each button's text and its position (x, y) in the window. Each tuple contains the button's label (like '7', '+', 'C', etc.) and its coordinates.

```python
for (text, x, y) in buttons:
```
- **Button Creation Loop**: This loop iterates over each button in the `buttons` list to create and place the buttons in the window.

```python
Button(master, text=text, width=11, height=4, relief='flat', bg='white', 
       command=lambda txt=text: self.click(txt)).place(x=x, y=y)
```
- **Button Definition**: This creates a Button widget for each item in the `buttons` list. It sets various properties:
  - `text`: the label on the button.
  - `width` and `height`: dimensions of the button.
  - `relief`: button style (flat, in this case).
  - `bg`: background color (white).
  - `command`: sets the action to be taken when the button is clicked. It uses a lambda function to call `self.click()` with the button's text as an argument.
  - `place(x, y)`: positions the button in the window.

```python
def click(self, value):
```
- **Button Click Method**: This method is called whenever a button is pressed. It takes the button's text value as an argument.

```python
if value == '=':
    self.solve()
```
- **Evaluate Equation**: If the button clicked is "=", it calls the `solve()` method to evaluate the expression.

```python
elif value == 'C':
    self.clear()
```
- **Clear Entry**: If the button is "C", it calls the `clear()` method to reset the display.

```python
else:
    self.entry_value += str(value)
    self.equation.set(self.entry_value)
```
- **Build Entry Value**: For all other button presses, it adds the button's text to `self.entry_value` and updates the display using `self.equation`.

```python
def clear(self):
```
- **Clear Method**: This method clears the current input and resets the display.

```python
self.entry_value = ''
self.equation.set('')
```
- **Reset Values**: It sets `self.entry_value` to an empty string and clears the display.

```python
def solve(self):
```
- **Solve Method**: This method evaluates the mathematical expression stored in `self.entry_value`.

```python
try:
    result = eval(self.entry_value)
```
- **Evaluate Expression**: It uses Python's built-in `eval()` function to compute the result of the expression. Note that `eval()` can be dangerous if the input is not sanitized, as it can execute arbitrary code.

```python
self.equation.set(result)
self.entry_value = str(result)
```
- **Display Result**: If evaluation is successful, it sets the display to the result and updates `self.entry_value` with the result for further calculations.

```python
except Exception as e:
    self.equation.set("Error")
    self.entry_value = ''
```
- **Error Handling**: If an exception occurs during evaluation (like a syntax error), it displays "Error" in the entry and resets `self.entry_value`.

```python
root = Tk()
```
- **Main Window Creation**: This creates the main window for the application.

```python
Calculator = Calculator(root)
```
- **Calculator Instance**: This creates an instance of the `Calculator` class, passing the main window (`root`) to it, which sets up the GUI.

```python
root.mainloop()
```
- **Event Loop**: This starts the Tkinter event loop, which keeps the window open and responsive until it is closed by the user.

### Summary

This code defines a simple calculator GUI using Tkinter. It creates buttons for digits and operations, allows users to input equations, evaluates them, and displays the results. The use of `StringVar` helps in updating the display dynamically, and methods are defined to handle button clicks, clear input, and evaluate expressions. The GUI is straightforward and functions as a basic calculator.
