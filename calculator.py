import tkinter as tk


def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    elif button_text == "⌫":  # Backspace button
        entry_var.set(current_text[:-1])
    else:
        entry_var.set(current_text + button_text)


root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#2c3e50")

#store input
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 28), justify='right', bd=10, relief=tk.FLAT, bg="#34495e", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=10, pady=10, sticky="nsew")

#button style
btn_style = {"font": ("Arial", 20), "bd": 3, "relief": tk.RAISED, "fg": "white", "bg": "#34495e", "activebackground": "#555"}

# Button layout
buttons = [
    ('C', '*', '/', '⌫'),
    ('7', '8', '9', '-'),
    ('4', '5', '6', '+'),
    ('1', '2', '3', '='),
    ('0', '.', '(', ')')
]


for r, row in enumerate(buttons, start=1):
    for c, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, command=lambda text=button_text: on_click(text), **btn_style)
        button.grid(row=r, column=c, ipadx=20, ipady=20, padx=5, pady=5, sticky="nsew")


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
