# ===== Daily Notes App =====
# A simple notes app that saves and displays notes from a file

while True:  # Infinite loop - runs until break is called
    print("\n===== Daily Notes App =====")  # Print menu title
    print("1. Add Note")                    # Option 1
    print("2. View Notes")                  # Option 2
    print("3. Exit")                        # Option 3

    choice = input("Enter your choice: ")   # Take input from user

    # ----- Option 1: Add a new note -----
    if choice == "1":
        note = input("Enter your note: ")     # Take note input from user
        with open("notes.txt", "a") as file:  # Open file in append mode
            file.write(note + "\n")           # Write note with a newline
        print("  Note saved successfully!")   # Success message

    # ----- Option 2: View all notes -----
    elif choice == "2":
        try:  # Handle error if file does not exist
            with open("notes.txt", "r") as file:  # Open file in read mode
                notes = file.readlines()           # Read all lines as a list
                if notes:  # Check if file has content
                    print("\n----- Your Notes -----")
                    for i, note in enumerate(notes, start=1):  # Number from 1
                        print(f"{i}. {note.strip()}")          # strip() removes \n
                    print("----------------------")
                else:  # If file is empty
                    print("📭 No notes found.")
        except FileNotFoundError:  # Runs if file does not exist
            print(" No notes file found. Add a note first.")

    # ----- Option 3: Exit the program -----
    elif choice == "3":
        print(" Exiting... Goodbye!")
        break  # Break out of the loop and end program

    # ----- Handle invalid input -----
    else:
        print(" Invalid choice! Please try again.")