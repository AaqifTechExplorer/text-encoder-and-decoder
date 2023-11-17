import tkinter as tk
from tkinter import ttk

mapping = {
    "a": "g", "b": "l", "c": "k", "d": "j", "e": "i",
    "f": "h", "g": "m", "h": "f", "i": "e", "j": "d",
    "k": "c", "s": "u", "t": "n", "l": "b", "m": "a",
    "n": "z", "o": "y", "p": "x", "q": "w", "r": "v",
    "u": "s", "w": "r", "v": "q", "x": "p", "y": "o",
    "z": "t"
}

def replace_characters(input_text, mapping):
    lowercased_text = input_text.lower()
    replaced_text = ''.join(mapping.get(char, char) for char in lowercased_text)
    return replaced_text

def encode_or_decode():
    choice = choice_var.get()

    if choice == 1:
        # Encryption
        user_input = input_entry.get()
        result = replace_characters(user_input, mapping)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Encrypted result: {result}")
        result_text.config(state=tk.DISABLED)

    elif choice == 2:
        # Decryption
        reverse_mapping = {v: k for k, v in mapping.items()}
        user_input = input_entry.get()
        result = replace_characters(user_input, reverse_mapping)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Decrypted result: {result}")
        result_text.config(state=tk.DISABLED)

    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid choice. Please enter either 1 or 2.")
        result_text.config(state=tk.DISABLED)

def copy_to_clipboard():
    result = result_text.get(1.0, tk.END)
    app.clipboard_clear()
    app.clipboard_append(result)
    app.update()

# Create the main application window
app = tk.Tk()
app.title("Encoder")

# Create and configure widgets
label = ttk.Label(app, text="Choose an option (1 for encryption, 2 for decryption):")
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

choice_var = tk.IntVar()
choice_entry = ttk.Entry(app, textvariable=choice_var)
choice_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

input_label = ttk.Label(app, text="Enter text:")
input_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

input_entry = ttk.Entry(app)
input_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

result_text = tk.Text(app, height=4, width=40, state=tk.DISABLED)
result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

process_button = ttk.Button(app, text="Process", command=encode_or_decode)
process_button.grid(row=3, column=0, padx=10, pady=10)

copy_button = ttk.Button(app, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=3, column=1, padx=10, pady=10)

# Configure column weights to make the layout flexible
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
app.mainloop()
