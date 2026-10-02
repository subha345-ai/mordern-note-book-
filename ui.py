import os
import sys
from datetime import datetime

FILE = "notes.txt"


class DailyNotesApp:
    """A modern Daily Notes App using file handling."""

    # ---------- Colors ----------
    HEADER = "\033[95m"
    BLUE   = "\033[94m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    RESET  = "\033[0m"
    BOLD   = "\033[1m"

    def __init__(self, filename=FILE):
        self.filename = filename
        self._ensure_file()

    def _ensure_file(self):
        """Create notes.txt if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("")

    # ---------- Menu ----------
    def menu(self):
        print(f"\n{self.HEADER}{self.BOLD}===== 📒 Daily Notes App ====={self.RESET}")
        print(f"{self.BLUE}1.{self.RESET} ➕ Add Note")
        print(f"{self.BLUE}2.{self.RESET} 📖 View Notes")
        print(f"{self.BLUE}3.{self.RESET} 🚪 Exit")

    # ---------- Open file in default editor ----------
    def _open_in_editor(self):
        """Open notes.txt in system's default text editor."""
        try:
            if sys.platform.startswith("win"):
                os.startfile(self.filename)
            elif sys.platform == "darwin":       # macOS
                os.system(f'open "{self.filename}"')
            else:                                 # Linux
                os.system(f'xdg-open "{self.filename}"')
        except Exception as e:
            print(f"{self.RED}⚠️ Could not open file: {e}{self.RESET}")

    # ---------- Option 1 ----------
    def add_note(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(f"\n[{timestamp}]\n")
            print(f"{self.GREEN}✅ notes.txt opened in editor.{self.RESET}")
            self._open_in_editor()
            input(f"{self.YELLOW}💾 Save the file, then press Enter to continue...{self.RESET}")
        except Exception as e:
            print(f"{self.RED}❌ Error: {e}{self.RESET}")

    # ---------- Option 2 ----------
    def view_notes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
            print(f"\n{self.HEADER}----- 📖 Your Notes -----{self.RESET}")
            print(content if content else f"{self.YELLOW}📭 No notes yet.{self.RESET}")
            print(f"{self.HEADER}--------------------------{self.RESET}")
        except FileNotFoundError:
            print(f"{self.RED}📭 notes.txt not found.{self.RESET}")

    # ---------- Main loop ----------
    def run(self):
        actions = {
            "1": self.add_note,
            "2": self.view_notes,
            "3": self.exit_app,
        }
        while True:
            self.menu()
            choice = input(f"{self.BOLD}Enter your choice: {self.RESET}").strip()
            action = actions.get(choice)
            if action:
                if action() is False:
                    break
            else:
                print(f"{self.RED}❌ Invalid choice! Try again.{self.RESET}")

    def exit_app(self):
        print(f"{self.GREEN}👋 Exiting... Goodbye!{self.RESET}")
        return False


# ---------- Entry point ----------
if __name__ == "__main__":
    app = DailyNotesApp()
    app.run()