import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output_label.config(text=f"Result: {result}")
    except Exception as e:
        output_label.config(text="Error: Invalid expression")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to input expression
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for button_text in buttons:
    tk.Button(root, text=button_text, width=5, command=lambda text=button_text: entry.insert(tk.END, text)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Button to clear the entry
tk.Button(root, text="C", width=5, command=lambda: entry.delete(0, tk.END)).grid(row=5, column=0)

# Button to calculate the result
tk.Button(root, text="=", width=5, command=calculate).grid(row=5, column=1, columnspan=3)

# Label to display the result
output_label = tk.Label(root, text="Result: ")
output_label.grid(row=6, column=0, columnspan=4)

root.mainloop()
