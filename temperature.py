import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temperature.get())
        if conversion_type.get() == "Fahrenheit to Celsius":
            result = (temp - 32) * 5 / 9
            label_result.config(text=f"Result: {result:.2f}°C")
        else:
            result = (temp * 9 / 5) + 32
            label_result.config(text=f"Result: {result:.2f}°F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

def reset_fields():
    entry_temperature.delete(0, tk.END)
    label_result.config(text="")
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x550")  # Window Size
root.resizable(True, True)
root.configure(bg="black")
glass_frame = tk.Frame(root, bg="#2c2c2c", bd=5, relief="ridge")  # Simulates transparency
glass_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=500)
title_label = tk.Label(glass_frame, text="Temperature Converter", font=("Georgia", 24, "bold"), bg="#2c2c2c", fg="pink")
title_label.pack(pady=30)

# Input Field for Temperature
entry_label = tk.Label(glass_frame, text="Enter Temperature:", font=("Bahnschrift SemiBold", 16), bg="#2c2c2c", fg="pale green")
entry_label.pack(pady=5)
entry_temperature = tk.Entry(glass_frame, font=("Helvetica", 22), width=10, borderwidth=4, 
                             relief="solid", justify="center", bg="#444", fg="white", insertbackground="white")
entry_temperature.pack(pady=15)

# Conversion Type Dropdown
conversion_type = tk.StringVar(value="Fahrenheit to Celsius")
conversion_dropdown = ttk.Combobox(glass_frame, textvariable=conversion_type, values=["Fahrenheit to Celsius", 
                                                                                      "Celsius to Fahrenheit"], state="readonly", width=20, font=("Helvetica", 16))
conversion_dropdown.pack(pady=15)

# Convert Button
convert_button = tk.Button(glass_frame, text="Convert", command=convert_temperature, font=("Avenir Next LT Pro", 16), 
                           bg="grey", fg="white", relief="raised", width=10)
convert_button.pack(pady=20)

# Result Label
label_result = tk.Label(glass_frame, text="", font=("Helvetica", 16, "bold"), fg="cyan", bg="#2c2c2c")
label_result.pack(pady=15)

# Reset Button
reset_button = tk.Button(glass_frame, text="Reset", command=reset_fields, font=("Helvetica", 16), 
                         bg="red", fg="white", relief="raised", width=20)
reset_button.pack(pady=10)

root.mainloop()
