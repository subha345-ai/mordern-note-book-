# ===== Daily Notes App with GUI =====
# A simple notes app using Tkinter for the user interface

import tkinter as tk                     # Import Tkinter for GUI
from tkinter import messagebox           # Import messagebox for popups

# ----- Function: Add a new note -----
def add_note():
    note = note_entry.get()              # Get text from the input field
    if note.strip() == "":               # Check if input is empty
        messagebox.showwarning("Warning", "Please write something!")
        return
    with open("notes.txt", "a") as file: # Open file in append mode
        file.write(note + "\n")          # Write note with a newline
    note_entry.delete(0, tk.END)         # Clear the input field
    messagebox.showinfo("Success", "✅ Note saved successfully!")

# ----- Function: View all notes -----
def view_notes():
    try:
        with open("notes.txt", "r") as file:   # Open file in read mode
            notes = file.readlines()           # Read all lines
        notes_box.delete(1.0, tk.END)          # Clear the text box
        if notes:                              # If notes exist
            for i, note in enumerate(notes, start=1):  # Number from 1
                notes_box.insert(tk.END, f"{i}. {note.strip()}\n")
        else:
            notes_box.insert(tk.END, "📭 No notes found.")
    except FileNotFoundError:                  # If file does not exist
        notes_box.delete(1.0, tk.END)
        notes_box.insert(tk.END, "📭 No notes file found. Add a note first.")

# ----- Function: Exit the app -----
def exit_app():
    root.destroy()                             # Close the window

# ----- Create main window -----
root = tk.Tk()                                 # Create main window
root.title("Daily Notes App")                  # Set window title
root.geometry("400x400")                       # Set window size

# ----- Title label -----
title_label = tk.Label(root, text="===== Daily Notes App =====",
                       font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# ----- Input field for note -----
note_entry = tk.Entry(root, width=40, font=("Arial", 11))
note_entry.pack(pady=5)

# ----- Add Note button -----
add_button = tk.Button(root, text="Add Note", width=15,
                       command=add_note, bg="lightgreen")
add_button.pack(pady=5)

# ----- View Notes button -----
view_button = tk.Button(root, text="View Notes", width=15,
                        command=view_notes, bg="lightblue")
view_button.pack(pady=5)

# ----- Text box to display notes -----
notes_box = tk.Text(root, height=10, width=40, font=("Arial", 10))
notes_box.pack(pady=10)

# ----- Exit button -----
exit_button = tk.Button(root, text="Exit", width=15,
                        command=exit_app, bg="salmon")
exit_button.pack(pady=5)

# ----- Run the app -----
root.mainloop()                                # Keep window open