import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def print_name():
    name = name_entry.get()
    n = int(times_entry.get())
    name_listbox.delete(0, tk.END)  # Clear the listbox before inserting new names
    for i in range(n):
        name_listbox.insert(tk.END, name)

# Initialize the main window
root = tk.Tk()
root.title("Name Printer")
root.geometry("400x300")

# Apply ttkbootstrap style
style = Style(theme='superhero')

# Create a frame to hold the widgets
frame = ttk.Frame(root, padding="10")
frame.pack(fill='both', expand=True)

# Name input
name_label = ttk.Label(frame, text="Enter your name:", font=("Verdana", 12))
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

name_entry = ttk.Entry(frame, style='success.TEntry', font=("Verdana", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Number of times input
times_label = ttk.Label(frame, text="How many times to print?", font=("Verdana", 12))
times_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

times_entry = ttk.Entry(frame, style='success.TEntry', font=("Verdana", 12))
times_entry.grid(row=1, column=1, padx=5, pady=5)

# Print button
print_button = ttk.Button(frame, text="Print Name", command=print_name, style='primary.TButton')
print_button.grid(row=2, column=0, columnspan=2, pady=10)

# Listbox to display names
name_listbox = tk.Listbox(frame, font=("Verdana", 12), height=10)
name_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

# Add weight to the rows and columns to make the Listbox expand with the window
frame.grid_rowconfigure(3, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
