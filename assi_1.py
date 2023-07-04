import re
import tkinter as tk
from tkinter import filedialog

def create_logical_view(file_path):
    # Read the text file
    with open(file_path, 'r') as file:
        document_text = file.read()

    # Preprocess the text
    document_text = re.sub(r'[^\w\s]', '', document_text.lower())
    document_tokens = document_text.split()

    # Create logical view based on word frequency
    word_counts = {}

    for word in document_tokens:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the logical view
    return sorted_word_counts

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        logical_view = create_logical_view(file_path)
        display_logical_view(logical_view)

def display_logical_view(logical_view):
    logical_view_text.delete(1.0, tk.END)
    for word, count in logical_view:
        logical_view_text.insert(tk.END, f"{word}: {count}\n")

# Create the main window
window = tk.Tk()
window.title("Logical View Creator")

# Create a button for browsing a file
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Create a text area for displaying the logical view
logical_view_text = tk.Text(window, height=20, width=50)
logical_view_text.pack()

# Run the main event loop
window.mainloop()