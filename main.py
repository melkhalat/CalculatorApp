import tkinter as tk              # tkinter for GUI
from tkinter import ttk           # themed widgets from tkinter
from simpleeval import simple_eval  # safe math expression evaluator 


# function runs whenever any calculator button is clicked
def handle_button_click(clicked_button_text):
    current_text = result_var.get()  # get current input 

    # if user clicks "=": evaluate the expression
    if clicked_button_text == "=":
        try:
            # replace custom math symbols with Python-compatible ones
            expression = current_text.replace("x", "*").replace("÷", "/")
            
            # use simple_eval to safely evaluate the expression
            result = simple_eval(expression)

            # convert result to an integer
            if result == int(result):
                result = int(result)

            # show the result 
            result_var.set(result)
        
        except Exception:
            # if the expression is invalid or causes error ex. division by 0 show "Error"
            result_var.set("Error")

    # reset clear button 
    elif clicked_button_text == "C":
        result_var.set("")

    # percentage button divides current value by 100
    elif clicked_button_text == "%":
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")

    # ± button flips the sign of the current number
    elif clicked_button_text == "±":
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")

    # for all other buttons append the button text to the input
    else:
        result_var.set(current_text + clicked_button_text)


# create the main GUI window
root = tk.Tk()
root.title("Calculator")

# stores the result and updates the entry widget
result_var = tk.StringVar()

# input display field at the top of the calculator
result_entry = ttk.Entry(
    root,
    textvariable=result_var,
    font=("Helvetica", 24),
    justify="right"  # align numbers to the right like a real calculator
)
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")  # span full width of top row

# define all calculator buttons and their grid positions
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

# configure button style 
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Helvetica", 16), width=10, height=4)

# create and position each button using grid layout
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1  # Some buttons span 2 columns (e.g., "0")

    # create a button and assign its click behavior
    button = ttk.Button(
        root,
        text=button_text,
        command=lambda text=button_text: handle_button_click(text),
        style="TButton"
    )
    
    # place the button in the grid with padding and expansion
    button.grid(
        row=row,
        column=col,
        columnspan=colspan,
        sticky="nsew",
        ipadx=10,
        ipady=4,
        padx=5,
        pady=5
    )

# make all rows and columns resizable to evenly scale the layout
for i in range(6):  # total 6 rows 
    root.grid_rowconfigure(i, weight=1) # 1 for display + 5 for buttons

for i in range(4):  # total 4 columns
    root.grid_columnconfigure(i, weight=1)

# set the fixed window size
width = 500
height = 700
root.geometry(f"{width}x{height}")

# prevent the user from resizing the window
root.resizable(False, False)

# connect keyboard keys to calculator actions
root.bind("<Return>", lambda event: handle_button_click("="))       # Enter key = evaluate
root.bind("<BackSpace>", lambda event: handle_button_click("C"))    # Backspace key = clear

# start the GUI event loop
root.mainloop()