import tkinter as tk
from tkinter import messagebox

# Initial set
my_set = {1, 2, 3, 4, 5}

# Function to remove item from the set
def remove_item():
    try:
        # Get the value from the entry widget
        item = int(entry.get())
        
        # Check if the item is in the set
        if item in my_set:
            my_set.remove(item)
            result_label.config(text=f"Item {item} removed. Updated set: {my_set}")
        else:
            result_label.config(text=f"Item {item} not found in the set.")
    except ValueError:
        # Handle case when input is not a valid integer
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Remove Item from Set")
root.geometry("400x400")

# Create and place the widgets
label = tk.Label(root, text="Enter an item to remove:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.pack(pady=10)

result_label = tk.Label(root, text=f"Current set: {my_set}")
result_label.pack(pady=10)

# Run the application
root.mainloop()
