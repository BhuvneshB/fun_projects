import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output_label.config(text=f"Result: {result}")
    except Exception as e:
        output_label.config(text="Error: Invalid expression")

# Create the main application window
root = tk.Tk()
root.title("Resizable Calculator")

# Entry widget to input expression
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for button_text in buttons:
    tk.Button(root, text=button_text, width=5, command=lambda text=button_text: entry.insert(tk.END, text)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Button to clear the entry
tk.Button(root, text="C", width=5, command=lambda: entry.delete(0, tk.END)).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Button to calculate the result
tk.Button(root, text="=", width=5, command=calculate).grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Label to display the result
output_label = tk.Label(root, text="Result: ")
output_label.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Make rows and columns resizable
for r in range(7):
    root.grid_rowconfigure(r, weight=1)
for c in range(4):
    root.grid_columnconfigure(c, weight=1)

root.mainloop()
